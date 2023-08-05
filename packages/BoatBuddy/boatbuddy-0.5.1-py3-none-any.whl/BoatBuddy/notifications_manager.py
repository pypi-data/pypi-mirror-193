import threading
import time
from enum import Enum

from BoatBuddy import globals, utils
from BoatBuddy.email_manager import EmailManager
from BoatBuddy.sound_manager import SoundManager, SoundType


class EntryType(Enum):
    METRIC = 'metric'
    MODULE = 'module'


class NotificationType(Enum):
    SOUND = 'sound'
    EMAIL = 'email'


class NotificationEntry:
    def __init__(self, timestamp, key, value, entry_type: EntryType, notification_types: [], severity, frequency,
                 cool_off_interval, configuration_range=None, interval=None):
        self._timestamp = timestamp
        self._key = key
        self._value = value
        self._entry_type = entry_type
        self._notification_types = notification_types
        self._severity = severity
        self._frequency = frequency
        self._cool_off_interval = cool_off_interval
        self._configuration_range = configuration_range
        self._interval = interval

    def get_timestamp(self):
        return self._timestamp

    def get_key(self):
        return self._key

    def get_value(self):
        return self._value

    def get_entry_type(self):
        return self._entry_type

    def get_severity(self):
        return self._severity

    def get_notification_types(self):
        return self._notification_types

    def get_frequency(self):
        return self._frequency

    def get_cool_off_interval(self):
        return self._cool_off_interval

    def get_configuration_range(self):
        return self._configuration_range

    def get_interval(self):
        return self._interval


class NotificationsManager:

    def __init__(self, options, sound_manager: SoundManager, email_manager: EmailManager):
        self._options = options
        self._sound_manager = sound_manager
        self._email_manager = email_manager
        self._notifications_queue = {}
        self._exit_signal = threading.Event()
        self._notifications_thread = threading.Thread(target=self._main_loop)
        self._mutex = threading.Lock()
        if self._options.notifications_module:
            self._notifications_thread.start()
            utils.get_logger().info('Notifications module successfully started!')

    def notify(self, key, value, entry_type):
        if not self._options.notifications_module:
            return

        if entry_type == EntryType.METRIC:
            notifications_rules = self._options.metrics_notifications_rules.copy()
        elif entry_type == EntryType.MODULE:
            notifications_rules = self._options.modules_notifications_rules.copy()
        else:
            return

        # First check if the provided key has a notification configuration
        if key not in notifications_rules:
            return

        # If an empty value is provided then return
        if value is None or value == '' or str(value).upper() == 'N/A':
            return

        # Next, check if the value is falls within a range where a notification should occur
        notification_configuration = notifications_rules[key]
        for severity in notification_configuration:
            if entry_type == EntryType.METRIC:
                configuration_range = notification_configuration[severity]['range']
                if configuration_range[1] >= utils.try_parse_float(value) > configuration_range[0]:
                    notification_interval = None
                    cool_off_interval = utils.try_parse_int(self._options.notification_cool_off_interval)
                    if notification_configuration[severity]['frequency'] == 'interval':
                        notification_interval = utils.try_parse_int(notification_configuration[severity]['interval'])
                    if 'cool-off-interval' in notification_configuration[severity]:
                        cool_off_interval = utils.try_parse_int(
                            notification_configuration[severity]['cool-off-interval'])
                    self._schedule_notification(key, value, entry_type,
                                                notification_configuration[severity]['notifications'],
                                                severity, notification_configuration[severity]['frequency'],
                                                cool_off_interval, configuration_range, notification_interval)
                    return
            elif entry_type == EntryType.MODULE:
                status = notification_configuration[severity]['status']
                if value == status:
                    notification_interval = None
                    cool_off_interval = utils.try_parse_int(self._options.notification_cool_off_interval)
                    if notification_configuration[severity]['frequency'] == 'interval':
                        notification_interval = utils.try_parse_int(notification_configuration[severity]['interval'])
                    if 'cool-off-interval' in notification_configuration[severity]:
                        cool_off_interval = utils.try_parse_int(
                            notification_configuration[severity]['cool-off-interval'])
                    self._schedule_notification(key, value, entry_type,
                                                notification_configuration[severity]['notifications'],
                                                severity, notification_configuration[severity]['frequency'],
                                                cool_off_interval, None, notification_interval)
                    return

        # If this point in the code is reached then notifications for this entry (if any) should be cleared
        self._delayed_clear_notification_entry(key)

    def _schedule_notification(self, key, value, entry_type, notification_types, severity, frequency, cool_off_interval,
                               configuration_range=None, interval=None):

        if key not in self._notifications_queue:
            # this is a new notification entry
            self._delayed_add_notification_entry(time.time(), key, value, entry_type, notification_types, severity,
                                                 frequency, cool_off_interval, configuration_range, interval)
        elif self._notifications_queue[key]['instance'].get_entry_type() == EntryType.METRIC and \
                self._notifications_queue[key]['instance'].get_configuration_range() != configuration_range or \
                self._notifications_queue[key]['instance'].get_entry_type() == EntryType.MODULE and \
                self._notifications_queue[key]['instance'].get_value() != value:
            # If there is already an entry in the que with the same key
            # and if the range provided is different as what is stored in memory
            # Or if the new entry is for a module and has a different value than the old one then
            # this notification is different and needs to be treated as new notification
            # thus we need clear the old notification entry and schedule a new one
            self._clear_notification_entry(key)
            self._delayed_add_notification_entry(time.time(), key, value, entry_type, notification_types, severity,
                                                 frequency, cool_off_interval, configuration_range, interval)

    def _process_notification(self, key, value, entry_type, notification_types, severity, frequency, cool_off_interval,
                              configuration_range, interval):
        if entry_type == EntryType.MODULE:
            utils.get_logger().info(f'Processing notification for module \'{key}\'')
        elif entry_type == EntryType.METRIC:
            utils.get_logger().info(f'Processing notification for metric with key \'{key}\'')

        if NotificationType.SOUND.value in notification_types:
            self._process_sound_notification(severity)

        if NotificationType.EMAIL.value in notification_types:
            self._process_email_notification(key, value, entry_type, severity, frequency, cool_off_interval,
                                             configuration_range, interval)

    def _process_clear_notification(self, key, notification_types, severity):
        if NotificationType.EMAIL.value in notification_types:
            self._process_clear_email_notification(key, severity)

    def _process_sound_notification(self, severity):
        if severity == 'alarm':
            self._sound_manager.play_sound_async(SoundType.ALARM)
        elif severity == 'warning':
            self._sound_manager.play_sound_async(SoundType.WARNING)

    def _process_email_notification(self, key, value, entry_type, severity, frequency, cool_off_interval,
                                    configuration_range, interval):
        try:
            configuration_range_str = 'N/A'
            interval_str = 'N/A'

            if configuration_range:
                configuration_range_str = str(configuration_range)

            if interval:
                interval_str = str(interval)

            body = 'N/A'
            subject = 'N/A'
            if entry_type == EntryType.MODULE:
                body = f'Notification triggered for the \'{key}\' module:\r\n' \
                       f'Status: {value}\r\nSeverity: {severity}' + \
                       f'\r\nFrequency: {frequency}\r\nConfiguration Range: ' \
                       f'{configuration_range_str}\r\nInterval: {interval_str} seconds\r\n ' \
                       f'Cool Off Interval: {cool_off_interval} seconds\r\n\r\n' \
                       f'--\r\n{globals.APPLICATION_NAME} ({globals.APPLICATION_VERSION})'
                subject = f'{globals.APPLICATION_NAME} - ({str(severity).upper()}) ' \
                          f'notification for \'{key}\' module'
            elif entry_type == EntryType.METRIC:
                body = f'Notification triggered for metric with key \'{key}\':\r\n' \
                       f'Value: {value}\r\nSeverity: {severity}' + \
                       f'\r\nFrequency: {frequency}\r\nConfiguration Range: ' \
                       f'{configuration_range_str}\r\nInterval: {interval_str} seconds\r\n ' \
                       f'Cool Off Interval: {cool_off_interval} seconds\r\n\r\n' \
                       f'--\r\n{globals.APPLICATION_NAME} ({globals.APPLICATION_VERSION})'
                subject = f'{globals.APPLICATION_NAME} - ({str(severity).upper()}) ' \
                          f'notification for metric \'{key}\''
            self._email_manager.send_email(subject, body)
            if entry_type == EntryType.MODULE:
                utils.get_logger().info(f'Email notification triggered '
                                        f'for the {key} module. Status: {value} '
                                        f'Severity: {severity} Frequency: {frequency} '
                                        f'Configuration Range: {configuration_range_str} Interval: {interval_str} '
                                        f'Cool Off Interval: {cool_off_interval}. An email will be sent out shortly!')
            elif entry_type == EntryType.METRIC:
                utils.get_logger().info(f'Email notification triggered '
                                        f'for the following {entry_type.value}. Key: {key} Value: {value} '
                                        f'Severity: {severity} Frequency: {frequency} '
                                        f'Configuration Range: {configuration_range_str} Interval: {interval_str} '
                                        f'Cool Off Interval: {cool_off_interval}. An email will be sent out shortly!')
        except Exception as e:
            utils.get_logger().error(f'Error while triggering email notification for {entry_type.value} '
                                     f'\'{key}\'. Details: {e}')

    def _process_clear_email_notification(self, key, severity):
        notification_entry = self._notifications_queue[key]['instance']
        try:
            body = f'Notification cleared for ' \
                   f'{notification_entry.get_entry_type().value} \'{key}\'\r\n\r\n' \
                   f'--\r\n{globals.APPLICATION_NAME} ({globals.APPLICATION_VERSION})'
            subject = f'{globals.APPLICATION_NAME} - ({str(severity).upper()}) cleared ' \
                      f'for {notification_entry.get_entry_type().value} \'{key}\''
            self._email_manager.send_email(subject, body)
            utils.get_logger().info(f'Notification cleared for '
                                    f' {notification_entry.get_entry_type().value} \'{key}\'. '
                                    f'An email will be sent out shortly!')
        except Exception as e:
            utils.get_logger().error(f'Error while clearing email notification '
                                     f'for {notification_entry.get_entry_type().value} \'{key}\'. Details: {e}')

    def _delayed_add_notification_entry(self, timestamp, key, value, entry_type, notification_types, severity,
                                        frequency, cool_off_interval, configuration_range, interval):

        new_notification_entry = NotificationEntry(timestamp, key, value, entry_type, notification_types, severity,
                                                   frequency, cool_off_interval, configuration_range, interval)

        self._mutex.acquire()
        self._notifications_queue[key] = {'instance': new_notification_entry, 'last_processed': None, 'to_clear': False}
        self._mutex.release()

        if entry_type == EntryType.METRIC:
            utils.get_logger().info(f'New notification added for metric with key \'{key}\', value \'{value}\', ' +
                                    f'severity \'{severity}\'')
        elif entry_type == EntryType.MODULE:
            utils.get_logger().info(f'New notification added for module \'{key}\', status \'{value}\', ' +
                                    f'severity \'{severity}\'')

    def _delayed_clear_notification_entry(self, key):
        if key not in self._notifications_queue:
            return

        # Mark it to be cleared
        self._mutex.acquire()
        self._notifications_queue[key]['last_processed'] = time.time()
        self._notifications_queue[key]['to_clear'] = True
        self._mutex.release()

        notification_entry = self._notifications_queue[key]['instance']
        cool_off_interval = utils.try_parse_int(notification_entry.get_cool_off_interval())
        utils.get_logger().info(f'Notification for {notification_entry.get_entry_type().value} with key \'{key}\' '
                                f'will be cleared after {cool_off_interval} seconds')

    def _clear_notification_entry(self, key):
        if key not in self._notifications_queue:
            return

        notification_entry = self._notifications_queue[key]['instance']
        self._process_clear_notification(key, notification_entry.get_notification_types(),
                                         notification_entry.get_severity())

        utils.get_logger().info(f'Cleared notification '
                                f'for {notification_entry.get_entry_type().value} with key \'{key}\'')

        # Remove the entry from memory
        self._mutex.acquire()
        self._notifications_queue.pop(key)
        self._mutex.release()

    def _main_loop(self):
        while not self._exit_signal.is_set():
            keys_for_entries_to_remove = []
            # for thread safety make a copy of the notification queue before starting with iterating over its contents
            self._mutex.acquire()
            for key in self._notifications_queue:
                notification_entry = self._notifications_queue[key]['instance']
                last_processed = self._notifications_queue[key]['last_processed']
                to_clear = self._notifications_queue[key]['to_clear']
                cool_off_interval = utils.try_parse_int(notification_entry.get_cool_off_interval())

                if to_clear and time.time() - last_processed > cool_off_interval:
                    # Clear the notification
                    self._clear_notification_entry(key)
                elif not to_clear and last_processed and time.time() - last_processed > cool_off_interval:
                    if notification_entry.get_entry_type() == EntryType.METRIC or \
                            (notification_entry.get_entry_type() == EntryType.MODULE and
                             notification_entry.get_frequency() == 'interval'):
                        # This is a recurring notification
                        # Process the notification
                        self._process_notification(key, notification_entry.get_value(),
                                                   notification_entry.get_entry_type(),
                                                   notification_entry.get_notification_types(),
                                                   notification_entry.get_severity(),
                                                   notification_entry.get_frequency(),
                                                   notification_entry.get_cool_off_interval(),
                                                   notification_entry.get_configuration_range(),
                                                   notification_entry.get_interval())

                    # Update the last_notified field value with the current time
                    self._notifications_queue[key]['last_processed'] = time.time()
                elif not to_clear and last_processed is None and \
                        time.time() - notification_entry.get_timestamp() > cool_off_interval:
                    # This is the first time the notification is processed
                    self._process_notification(key, notification_entry.get_value(),
                                               notification_entry.get_entry_type(),
                                               notification_entry.get_notification_types(),
                                               notification_entry.get_severity(),
                                               notification_entry.get_frequency(),
                                               notification_entry.get_cool_off_interval(),
                                               notification_entry.get_configuration_range(),
                                               notification_entry.get_interval())

                    if notification_entry.get_entry_type() == EntryType.MODULE:
                        # If this is a module notification then keep it in the queue until it is cleared
                        # Hence we only need to update the last processed field at this stage
                        self._notifications_queue[key]['last_processed'] = time.time()
                    elif notification_entry.get_entry_type() == EntryType.METRIC:
                        if notification_entry.get_frequency() == 'once':
                            keys_for_entries_to_remove.append(key)
                        elif notification_entry.get_frequency() == 'interval':
                            # This is a recurring notification
                            # Update the last_notified field value with the current time
                            self._notifications_queue[key]['last_processed'] = time.time()

            # Remove all processed entries with frequency == 'once'
            if len(keys_for_entries_to_remove) > 0:
                for key in keys_for_entries_to_remove:
                    self._notifications_queue.pop(key)
            self._mutex.release()

            time.sleep(1)  # Sleep for one second

    def finalize(self):
        if not self._options.notifications_module:
            return

        self._exit_signal.set()

        if len(self._notifications_queue) > 0:
            self._mutex.acquire()
            self._notifications_queue.clear()
            self._mutex.release()
