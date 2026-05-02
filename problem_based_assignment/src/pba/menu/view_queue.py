from ..emergency_queue import EmergencyQueue
from .menu_option import MenuOption


class ViewQueue(MenuOption):

    def __init__(self, emergency_queue: EmergencyQueue):
        self.emergency_queue = emergency_queue

    def __str__(self) -> str:
        return 'View Emergency Queue'

    def execute(self):
        '''Command-line menu option execution to display the emergency queue.'''

        patients = self.emergency_queue.view_queue()
        if patients:
            message = f'{'Order':<6} {'Name':<40} {'Age':<5} {'Condition':<25}'
            message += '\n' + ('-' * 75)
            idx = 0
            for patient in patients:
                idx += 1
                order = 'First' if idx == 1 else str(idx)
                message += f'\n{order:<6} {patient.name:<40} {patient.age:<5} {patient.condition:<25}'
        else:
            message = 'No patients in the emergency queue to serve.'
        return message