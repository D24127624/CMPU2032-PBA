from ..patient_records import PatientRecords
from .menu_option import MenuOption


class ViewRecords(MenuOption):

    def __init__(self, patient_records: PatientRecords):
        self.patient_records = patient_records

    def __str__(self) -> str:
        return 'View Patients'

    def execute(self):
        '''Command-line menu option execution to display all available patient records.'''

        patients = self.patient_records.list_patients()
        if patients:
            message = f'{'ID':<5} {'Name':<40} {'Age':<5} {'Condition':<25}'
            message += '\n' + ('-' * 75)
            for patient in patients:
                message += f'\n{patient.id:<5} {patient.name:<40} {patient.age:<5} {patient.condition:<25}'
        else:
            message = 'No patient records found.'
        return message
