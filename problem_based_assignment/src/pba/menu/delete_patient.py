from ..patient_records import PatientRecords
from .menu_option import MenuOption


class DeletePatient(MenuOption):

    def __init__(self, patient_records: PatientRecords):
        self.patient_records = patient_records

    def __str__(self) -> str:
        return 'Delete Patient'

    def execute(self):
        '''Command-line menu option execution to remove a patient from the records linked-list.'''

        patient_id = int(input('\n\nEnter patient ID to delete: '))

        # delete the patient from the patient records
        patient = self.patient_records.delete_patient(patient_id)
        if patient:
            return f'Patient ID ({patient.id}) deleted successfully.'
        else:
            return f'Patient ID ({patient_id}) not found.'
