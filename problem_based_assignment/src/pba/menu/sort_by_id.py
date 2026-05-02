from ..patient_records import PatientRecords
from ..sorting.merge_sort import MergeSort
from .menu_option import MenuOption


class SortById(MenuOption):

    def __init__(self, patient_records: PatientRecords):
        self.patient_records = patient_records

    def __str__(self) -> str:
        return 'Sort by ID (Merge Sort)'

    def execute(self):
        '''Command-line menu option execution to sort the patient records linked-list.'''

        if self.patient_records.head:
            MergeSort(self.patient_records, 'id').sort()
            return 'Patient records have been sorted by ID successfully.'
        else:
            return 'Cannot sort the patient records, asnone were found.'
