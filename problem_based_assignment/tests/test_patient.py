import unittest

from pba.patient import Patient


class TestPatient(unittest.TestCase):

    def test_patient_creation(self):
        patient = Patient(1234, 'Patient One', 36, 'Nausea')
        self.assertEqual(patient.id, 1234)
        self.assertEqual(patient.name, 'Patient One')
        self.assertEqual(patient.age, 36)
        self.assertEqual(patient.condition, 'Nausea')

    def test_patient_str(self):
        patient = Patient(1234, 'Patient One', 36, 'Nausea')
        self.assertEqual(str(patient), 'Patient(ID=1234, name=Patient One, age=36, condition=Nausea)')

    def test_age_is_int(self):
        with self.assertRaises(TypeError):
            Patient(5678, 'Patient Two', 'thirty-Three', 'Cold')
