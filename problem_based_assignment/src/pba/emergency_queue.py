from .patient import Patient


class EmergencyQueue:

    def __init__(self):
        self.queue = []

    def enqueue_patient(self, patient: Patient) -> bool:
        '''Adds a patient to the emergency queue if they are not already in the queue.'''

        # ensure patient is not already in the queue
        if patient in self.queue:
            return False
        # add the patient to the end of the queue
        self.queue.append(patient)
        return True

    def dequeue_patient(self) -> Patient | None:
        '''Dequeues the first patient in the emergency queue and returns their information.'''

        return None if self.is_empty() else self.queue.pop(0)

    def view_queue(self) -> list[Patient]:
        '''Returns a list of all patients currently in the emergency queue.'''

        return [patient for patient in self.queue]

    def is_empty(self):
        '''Check to determine if the queue is empty.'''

        return not self.queue
