import random

from .patient import Patient


# Patient Records Management (linked-list)

class LinkNode:
    '''Node class used to hold the respective patient record and reference to the next node in the linked list.'''

    def __init__(self, patient: Patient):
        self.data = patient
        self.next = None

    def __str__(self):
        '''Override the default to-string method to return a human-readable string.'''
        return f'Node(data={self.data}, next={None if self.next is None else self.next.data})'


class PatientRecords:
    '''Patient Records linked-list implemnentation, with several specific methods to manage the list.'''

    def __init__(self):
        self.patient_id = 0
        self.head = None
        self.tail = None

    def add_patient(self, patient: Patient) -> bool:
        '''Adding a new paient node to the end of the linked-list.'''

        # ensure the patient ID is unique
        if self.find_patient(patient.id):
            return False

        node = LinkNode(patient)
        if self.tail:
            self.tail.next = node
        else:
            self.head = node
        self.tail = node
        return True

    def delete_patient(self, patient_id: int) -> Patient | None:
        '''Deletes a patient from the linked-list based the respective patient ID.'''

        previous = None
        node = self.head
        # iterate over the linked-list to find the patient to be removed
        while node:
            # check match with patient ID
            if node.data.id == patient_id:
                # is match on the HEAD node
                if self.head == node:
                    self.head = node.next
                # is matched with last node
                elif self.tail == node:
                    previous.next = node.next
                    self.tail = previous
                # is matched with any other node
                else:
                    previous.next = node.next
                return node.data
            # check to the next node
            previous = node
            node = node.next
        # patient ID was not found
        return None

    def find_patient(self, patient_id: int) -> Patient | None:
        '''Search for a patient in the linked-list based on the respective patient ID.'''

        node = self.head
        # iterate over the linked-list to find the patient
        while node:
            if node.data.id == patient_id:
                return node.data
            node = node.next
        return None

    def list_patients(self) -> list[Patient]:
        '''returns a list of all patients in the linked-list.'''

        patients = []
        node = self.head
        # extract each patient in the linked-list into a simple list
        while node:
            patients.append(node.data)
            node = node.next
        return patients

    def clear_list(self):
        '''Clears the linked-list of all patient records.'''
        self.head = None
        self.tail = None

    def next_id(self) -> int:
        '''Generate the next ID for a patient.'''

        self.patient_id = random.randint(2, 9000) + 999
        return self.patient_id
