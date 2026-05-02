import unittest

from pba.patient import Patient
from pba.patient_records import PatientRecords
from pba.sorting.merge_sort import MergeSort


class TestMergeSort(unittest.TestCase):

    def setUp(self):
        self.patient1 = Patient(1234, 'Patient One', 40, 'Nausea')
        self.patient2 = Patient(5678, 'Patient Two', 52, 'Fever')
        self.patient3 = Patient(9876, 'Patient Three', 36, 'Cold')
        self.patient_records = PatientRecords()
        self.patient_records.add_patient(self.patient2)
        self.patient_records.add_patient(self.patient3)
        self.patient_records.add_patient(self.patient1)

    def test_merge_sort_with_id(self):
        self.assertEqual(self.patient_records.head.data, self.patient2)
        self.assertEqual(self.patient_records.tail.data, self.patient1)
        sorter = MergeSort(self.patient_records, key='id')
        sorter.sort()
        self.assertEqual(self.patient_records.head.data, self.patient1)
        self.assertEqual(self.patient_records.tail.data, self.patient3)

    def test_merge_sort_with_age(self):
        self.assertEqual(self.patient_records.head.data, self.patient2)
        self.assertEqual(self.patient_records.tail.data, self.patient1)
        sorter = MergeSort(self.patient_records, key='age')
        sorter.sort()
        self.assertEqual(self.patient_records.head.data, self.patient3)
        self.assertEqual(self.patient_records.tail.data, self.patient2)


