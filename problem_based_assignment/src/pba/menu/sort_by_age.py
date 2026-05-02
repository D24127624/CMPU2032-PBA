from ..patient_records import PatientRecords
from ..sorting.shell_sort import ShellSort
from .menu_option import MenuOption


class SortByAge(MenuOption):

    def __init__(self, patient_records: PatientRecords):
        self.patient_records = patient_records

    def __str__(self) -> str:
        return 'Sort by Age (Shell Sort)'

    def execute(self):
        '''Command-line menu option execution to sort the patient records linked-list.'''

        if self.patient_records.head:
            ShellSort(self.patient_records, 'age').sort()
            return 'Patient records have been sorted by AGE successfully.'
        else:
            return 'Cannot sort the patient records, asnone were found.'
