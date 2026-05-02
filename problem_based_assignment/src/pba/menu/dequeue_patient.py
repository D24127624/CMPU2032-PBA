from ..emergency_queue import EmergencyQueue
from .menu_option import MenuOption


class DequeuePatient(MenuOption):

    def __init__(self, emergency_queue: EmergencyQueue):
        self.emergency_queue = emergency_queue

    def __str__(self) -> str:
        return 'Process next Emergency Patient'

    def execute(self):
        '''Command-line menu option execution to serve the next patient in the emergency queue.'''

        # dequeue the next patient to serve
        patient = self.emergency_queue.dequeue_patient()
        if patient:
            return f'Now serving next patient: {patient.name} (age: {patient.age}, condition: {patient.condition})'
        else:
            return 'No patients in the emergency queue to serve.'
