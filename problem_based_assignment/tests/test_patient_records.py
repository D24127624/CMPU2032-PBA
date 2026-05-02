import unittest

from pba.patient import Patient
from pba.patient_records import PatientRecords


class TestPatientRecords(unittest.TestCase):
    def setUp(self):
        self.patient1 = Patient(1234, 'Patient One', 36, 'Nausea')
        self.patient2 = Patient(5678, 'Patient Two', 40, 'Fever')
        self.patient3 = Patient(9876, 'Patient Three', 52, 'Cold')
        self.patient_records = PatientRecords()

    def test_add_patient(self):
        self.patient_records.add_patient(self.patient1)
        self.assertEqual(self.patient_records.head.data, self.patient1)
        self.assertEqual(self.patient_records.head.data, self.patient_records.tail.data)
        self.patient_records.add_patient(self.patient2)
        self.assertEqual(self.patient_records.head.next.data, self.patient2)
        self.assertEqual(self.patient_records.head.next.data, self.patient_records.tail.data)
        self.patient_records.add_patient(self.patient3)
        self.assertEqual(self.patient_records.head.next.data, self.patient2)
        self.assertEqual(self.patient_records.head.next.next.data, self.patient3)
        self.assertEqual(self.patient_records.head.next.next.data, self.patient_records.tail.data)

    def test_list_patients(self):
        self.assertEqual(self.patient_records.list_patients(), [])
        self.patient_records.add_patient(self.patient1)
        self.patient_records.add_patient(self.patient2)
        self.patient_records.add_patient(self.patient3)
        patients = self.patient_records.list_patients()
        self.assertEqual(len(patients), 3)
        self.assertEqual(self.patient_records.head.data, patients[0])
        self.assertEqual(self.patient_records.head.next.data, patients[1])
        self.assertEqual(self.patient_records.head.next.next.data, patients[2])

    def test_delete_patient(self):
        self.assertFalse(self.patient_records.delete_patient(1234))
        self.patient_records.add_patient(self.patient1)
        self.patient_records.add_patient(self.patient2)
        self.patient_records.add_patient(self.patient3)
        self.assertTrue(self.patient_records.delete_patient(1234)) # remove first element
        self.assertEqual(self.patient_records.head.data, self.patient2)
        self.patient_records.add_patient(self.patient1)
        self.assertTrue(self.patient_records.delete_patient(9876)) # remove middle element
        self.assertEqual(self.patient_records.head.next.data, self.patient1)
        self.patient_records.add_patient(self.patient3)
        self.assertTrue(self.patient_records.delete_patient(9876)) # remove last element
        self.assertEqual(self.patient_records.head.next.data, self.patient1)

    def test_find_patient(self):
        self.patient_records.add_patient(self.patient1)
        self.patient_records.add_patient(self.patient2)
        self.patient_records.add_patient(self.patient3)
        self.assertIsNone(self.patient_records.find_patient(9999))
        self.assertEqual(self.patient_records.find_patient(9876), self.patient3)
        self.assertEqual(self.patient_records.find_patient(5678), self.patient2)
        self.assertEqual(self.patient_records.find_patient(1234), self.patient1)
