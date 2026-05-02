from ..patient import Patient
from ..patient_records import PatientRecords


class ShellSort:

    def __init__(self, patient_records: PatientRecords, key: str):
        self.patient_records = patient_records
        self.key = key

    def sort(self):
        '''Perform the sorting on the patient records linked-list.'''

        # dont continue if the list is empty
        if self.patient_records.head is None:
            return
        # convert the linked list to an array for sorting
        patients = self.__convert_to_array()
        no_patients = len(patients)
        gap = no_patients // 2
        # perform the shell sort algorithm on the array
        while gap > 0:
            for i in range(gap, no_patients):
                temp = patients[i]
                j = i
                # compare elements gap positions apart
                while j >= gap and self.__get_value(patients[j - gap]) > self.__get_value(temp):
                    patients[j] = patients[j - gap]
                    j -= gap
                patients[j] = temp
            gap //= 2
        # rebuild the linked list from the sorted array
        self.__rebuild_linked_list(patients)

    def __convert_to_array(self) -> list[Patient]:
        '''Helper method to convert the linked list of patient records into an array for sorting.'''

        patients = []
        node = self.patient_records.head
        while node:
            patients.append(node.data)
            node = node.next
        return patients

    def __get_value(self, value):
        '''Helper method to get object value for comparison.'''

        return getattr(value, self.key)

    def __rebuild_linked_list(self, patients: list[Patient]):
        '''Helper method to rebuild the linked list of patient records from the sorted array.'''

        self.patient_records.clear_list()
        for patient in patients:
            self.patient_records.add_patient(patient)
