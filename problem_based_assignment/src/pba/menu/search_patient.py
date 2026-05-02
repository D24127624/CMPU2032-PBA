from ..patient_records import PatientRecords
from .menu_option import MenuOption


class SearchPatient(MenuOption):

    def __init__(self, patient_records: PatientRecords):
        self.patient_records = patient_records

    def __str__(self) -> str:
        return 'Search Patient'

    def execute(self):
        '''Command-line menu option execution to search for a patient in the records linked-list.'''

        patient_id = int(input('\n\nEnter patient ID to find: '))

        # find for patient in the patient records
        patient = self.patient_records.find_patient(patient_id)
        if patient:
            message = f'{'ID':<5} {'Name':<40} {'Age':<5} {'Condition':<25}'
            message += '\n' + ('-' * 75)
            message += f'\n{patient.id:<5} {patient.name:<40} {patient.age:<5} {patient.condition:<25}'
        else:
            message = f'No patient records found for ID ({patient_id}).'
        return message
