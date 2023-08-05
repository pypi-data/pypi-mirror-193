import time

from rich.console import Console
from rich.layout import Layout
from rich.live import Live
from rich.panel import Panel
from rich.spinner import Spinner
from rich.style import Style
from rich.table import Table
from rich.text import Text

from BoatBuddy import utils
from BoatBuddy.email_manager import EmailManager
from BoatBuddy.generic_plugin import PluginStatus
from BoatBuddy.notifications_manager import NotificationsManager, EntryType
from BoatBuddy.plugin_manager import PluginManager, PluginManagerStatus
from BoatBuddy.sound_manager import SoundManager


class ConsoleManager:

    def __init__(self, options, plugin_manager: PluginManager, notifications_manager: NotificationsManager,
                 sound_manager: SoundManager, email_manager: EmailManager):
        self._options = options
        self._plugin_manager = plugin_manager
        self._notifications_manager = notifications_manager
        self._sound_manager = sound_manager
        self._email_manager = email_manager

        self._console = Console()

        with Live(self._make_layout(), refresh_per_second=4) as live:
            try:
                while True:
                    time.sleep(0.5)
                    live.update(self._make_layout())
            except KeyboardInterrupt:  # on keyboard interrupt...
                utils.get_logger().warning("Ctrl+C signal detected!")
            finally:
                # Notify the plugin manager
                self._plugin_manager.finalize()
                # Notify the notifications manager
                self._notifications_manager.finalize()
                # Notify the sound manager
                self._sound_manager.finalize()
                # Notify the email manager
                self._email_manager.finalize()

    def _make_header(self) -> Layout:
        application_name = utils.get_application_name()
        application_version = utils.get_application_version()
        curr_time = time.strftime("%H:%M", time.localtime())
        status = self._plugin_manager.get_status()

        status_renderable = None
        application_info_renderable = None
        local_time_renderable = None
        if status == PluginManagerStatus.IDLE:
            status_style = Style(color='bright_white', bgcolor='default')
            status_renderable = Spinner('simpleDots', text=Text('Idle', style=status_style))
            application_info_style = Style(color='blue', bgcolor='default', bold=True)
            application_info_renderable = Text(f'{application_name} ({application_version})',
                                               style=application_info_style)
            local_time_style = Style(color='bright_yellow', bgcolor='default')
            local_time_renderable = Text(f'Local time: {curr_time}',
                                         style=local_time_style)
        elif status == PluginManagerStatus.SESSION_ACTIVE:
            status_style = Style(color='bright_white', bgcolor='red')
            status_renderable = Spinner('earth', text=Text('Session active', style=status_style))
            application_info_style = Style(color='bright_white', bgcolor='red', bold=True)
            application_info_renderable = Text(f'{application_name} ({application_version})',
                                               style=application_info_style)
            local_time_style = Style(color='bright_white', bgcolor='red')
            local_time_renderable = Text(f'Local time: {curr_time}',
                                         style=local_time_style)

        grid = Table.grid(expand=True)
        grid.add_column(justify="left")
        grid.add_column(justify="center", ratio=1, style='blue')
        grid.add_column(justify="right", style="bright_yellow")
        grid.add_row(
            status_renderable,
            application_info_renderable,
            local_time_renderable
        )
        return Layout(grid)

    def _make_summary(self) -> Layout:
        layout = Layout()
        layout.split_column(
            Layout(name="summary_header", size=5),
            Layout(name="summary_body", ratio=1),
        )

        summary_header_table = Table.grid(expand=True)
        summary_header_table.add_column()
        summary_header_table.add_column()
        summary_header_key_value_list = self._plugin_manager.get_filtered_session_clock_metrics()
        counter = 0
        while counter < len(summary_header_key_value_list):
            key = list(summary_header_key_value_list.keys())[counter]

            if counter + 1 < len(summary_header_key_value_list):
                next_key = list(summary_header_key_value_list.keys())[counter + 1]
                summary_header_table.add_row(
                    f'[bright_white]{key}: {summary_header_key_value_list[key]}[/bright_white]',
                    f'[bright_white]{next_key}: {summary_header_key_value_list[next_key]}[/bright_white]')
            else:
                summary_header_table.add_row(
                    f'[bright_white]{key}: {summary_header_key_value_list[key]}[/bright_white]', '')
            counter += 2

        layout["summary_header"].update(
            Layout(Panel(summary_header_table, title=f'{self._plugin_manager.get_session_name()}')))

        summary_body_table = Table.grid(expand=True)
        summary_body_table.add_column()
        summary_body_table.add_column()
        summary_key_value_list = self._plugin_manager.get_filtered_summary_metrics()
        counter = 0
        while counter < len(summary_key_value_list):
            key = list(summary_key_value_list.keys())[counter]

            if counter + 1 < len(summary_key_value_list):
                next_key = list(summary_key_value_list.keys())[counter + 1]
                summary_body_table.add_row(f'[bright_white]{key}: {summary_key_value_list[key]}[/bright_white]',
                                           f'[bright_white]{next_key}: {summary_key_value_list[next_key]}[/bright_white]')
            else:
                summary_body_table.add_row(f'[bright_white]{key}: {summary_key_value_list[key]}[/bright_white]', '')
            counter += 2

        layout["summary_body"].update(Layout(Panel(summary_body_table,
                                                   title=f'Session Summary')))
        return layout

    @staticmethod
    def _make_footer() -> Panel:
        footer_table = Table.grid(expand=True)
        footer_table.add_column()
        last_log_entries = utils.get_last_log_entries(3)
        for entry in last_log_entries:
            colour = 'default'
            if 'INFO' in str(entry).upper():
                colour = 'green'
            elif 'WARNING' in str(entry).upper():
                colour = 'yellow'
            elif 'ERROR' in str(entry).upper():
                colour = 'red'
            footer_table.add_row(f'[{colour}]{entry}[/{colour}]')
        return Panel(footer_table, title=f'Last 3 log entries')

    def _make_key_value_table(self, title, key_value_list) -> Panel:
        table = Table.grid(expand=True)
        table.add_column()
        colour = 'default'

        for key in key_value_list:
            if self._options.notification_console:
                colour = utils.get_colour_for_key_value_in_dictionary(self._options.metrics_colouring_scheme, key,
                                                                      key_value_list[key])
            if colour != 'default':
                table.add_row(f'[b][{colour}]{key}: ' +
                              f'{key_value_list[key]}[/{colour}][/b]')
            else:
                table.add_row(f'[bright_white]{key}: ' +
                              f'{key_value_list[key]}[/bright_white]')
            self._notifications_manager.notify(key, key_value_list[key], EntryType.METRIC)
        return Panel(table, title=title)

    def _make_layout(self) -> Layout:
        layout = Layout()

        if self._options.log_module and self._options.console_show_log:
            layout.split_column(
                Layout(name="header", size=1),
                Layout(name="body", ratio=1),
                Layout(name="footer", size=5)
            )

            layout["footer"].update(self._make_footer())
        else:
            layout.split_column(
                Layout(name="header", size=1),
                Layout(name="body", ratio=1),
            )

        layout["header"].update(self._make_header())

        # Add the plugins layout for the loaded plugins
        victron_layout = None
        gps_layout = None
        nmea_layout = None
        summary_layout = None

        if self._options.victron_module and self._options.console_show_victron_plugin:
            victron_layout = Layout(name="victron")
            # Populate the victron layout
            plugin_status_str = self._get_plugin_status_str(self._plugin_manager.get_victron_plugin_status())
            victron_layout.update(self._make_key_value_table('Victron ESS ' + plugin_status_str,
                                                             self._plugin_manager.get_filtered_victron_metrics()))

        if self._options.gps_module and self._options.console_show_gps_plugin:
            gps_layout = Layout(name="gps")
            # Populate the NMEA layout
            plugin_status_str = self._get_plugin_status_str(self._plugin_manager.get_gps_plugin_status())
            gps_layout.update(self._make_key_value_table('GPS Module ' + plugin_status_str,
                                                         self._plugin_manager.get_filtered_gps_metrics()))

        if self._options.nmea_module and self._options.console_show_nmea_plugin:
            nmea_layout = Layout(name="nmea")
            # Populate the NMEA layout
            plugin_status_str = self._get_plugin_status_str(self._plugin_manager.get_nmea_plugin_status())
            nmea_layout.update(self._make_key_value_table('NMEA0183 Network ' + plugin_status_str,
                                                          self._plugin_manager.get_filtered_nmea_metrics()))

        if self._plugin_manager.get_status() == PluginManagerStatus.SESSION_ACTIVE:
            summary_layout = Layout(name="summary", ratio=2)
            summary_layout.update(self._make_summary())

        layouts_list = []
        if victron_layout:
            layouts_list.append(victron_layout)

        if nmea_layout:
            layouts_list.append(nmea_layout)

        if gps_layout:
            layouts_list.append(gps_layout)

        if summary_layout:
            layouts_list.append(summary_layout)

        layout["body"].split_row(*layouts_list)

        return layout

    @staticmethod
    def _get_plugin_status_str(plugin_status: PluginStatus):
        plugin_status_str = ''
        if plugin_status == PluginStatus.DOWN:
            plugin_status_str = '[red](Down)[/red]'
        elif plugin_status == PluginStatus.STARTING:
            plugin_status_str = '[bright_yellow](Starting)[/bright_yellow]'
        elif plugin_status == PluginStatus.RUNNING:
            plugin_status_str = '[green](Running)[/green]'
        return plugin_status_str
