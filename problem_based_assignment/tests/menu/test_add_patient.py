import unittest
from unittest.mock import patch, MagicMock

from pba.menu.add_patient import AddPatient


class TestAddPatient(unittest.TestCase):

    def setUp(self):
        self.patient_records = MagicMock()
        self.patient_records.add_patient.return_value = True
        self.patient_records.next_id.return_value = 1234
        self.add_patient_option = AddPatient(self.patient_records)

    @patch('builtins.input', side_effect=['Test Patient', '40', 'Fever'])
    def test_add_patient_success(self, mock_input):
        message = self.add_patient_option.execute()
        self.patient_records.add_patient.assert_called_once()
        self.assertEqual(message, 'Patient ID (1234) added successfully.')

    @patch('builtins.input', side_effect=['Test Patient', '40', 'Fever'])
    def test_add_patient_failed(self, mock_input):
        self.patient_records.add_patient.return_value = False
        message = self.add_patient_option.execute()
        self.patient_records.add_patient.assert_called_once()
        self.assertEqual(message, 'Patient ID (1234) already exists! Please use a unique ID.')

    @patch('builtins.input', side_effect=['Test Patient', 'Fourty', 'Fever'])
    def test_add_patient_bad_input(self, mock_input):
        with self.assertRaises(ValueError):
            self.add_patient_option.execute()
        self.patient_records.add_patient.assert_not_called()
