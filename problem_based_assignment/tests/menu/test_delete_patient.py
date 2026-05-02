import unittest
from unittest.mock import patch, MagicMock

from pba.menu.delete_patient import DeletePatient
from pba.patient import Patient


class TestDeletePatient(unittest.TestCase):

    def setUp(self):
        self.patient_records = MagicMock()
        self.patient_records.delete_patient.return_value = Patient(1234, 'Test Patient', 40, 'Fever')
        self.delete_patient_option = DeletePatient(self.patient_records)

    @patch('builtins.input', side_effect=['1234'])
    def test_delete_patient_success(self, mock_input):
        message = self.delete_patient_option.execute()
        self.patient_records.delete_patient.assert_called_once()
        self.assertEqual(message, 'Patient ID (1234) deleted successfully.')

    @patch('builtins.input', side_effect=['1234'])
    def test_delete_patient_not_found(self, mock_input):
        self.patient_records.delete_patient.return_value = None
        message = self.delete_patient_option.execute()
        self.patient_records.delete_patient.assert_called_once()
        self.assertEqual(message, 'Patient ID (1234) not found.')
