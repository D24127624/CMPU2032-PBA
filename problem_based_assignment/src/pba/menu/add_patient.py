from ..patient import Patient
from ..patient_records import PatientRecords
from .menu_option import MenuOption


class AddPatient(MenuOption):

    def __init__(self, patient_records: PatientRecords):
        self.patient_records = patient_records

    def __str__(self) -> str:
        return 'Add Patient'

    def execute(self) -> str:
        '''Command-line menu option execution to add a patient to the records linked-list.'''

        name = input('\n\nEnter Name: ')
        age = int(input('Enter Age: '))
        condition = input('Enter Condition: ')

        # create a new patient instance and add it to the patient records
        patient = Patient(self.patient_records.next_id(), name, age, condition)
        if self.patient_records.add_patient(patient):
            return f'Patient ID ({patient.id}) added successfully.'
        else:
            return f'Patient ID ({patient.id}) already exists! Please use a unique ID.'
