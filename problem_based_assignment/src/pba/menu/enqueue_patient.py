from ..emergency_queue import EmergencyQueue
from ..patient_records import PatientRecords
from .menu_option import MenuOption


class EnqueuePatient(MenuOption):

    def __init__(self, emergency_queue: EmergencyQueue, patient_records: PatientRecords):
        self.emergency_queue = emergency_queue
        self.patient_records = patient_records

    def __str__(self) -> str:
        return 'Add Emergency Patient'

    def execute(self):
        '''Command-line menu option execution to add a patient to the emergency queue.'''

        patient_id = int(input('\n\nEnter patient ID to queue: '))

        # find for patient in the patient records
        patient = self.patient_records.find_patient(patient_id)
        if patient is None:
            return f'No patient records found for ID ({patient_id})! Cannot add to emergency queue.'
        elif self.emergency_queue.enqueue_patient(patient):
            return f'Patient ID ({patient.id}) added to the emergency queue successfully.'
        else:
            return f'Patient ID ({patient.id}) is already in the emergency queue! Cannot add duplicate entries.'
