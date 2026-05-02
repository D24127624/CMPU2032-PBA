

import unittest
from unittest.mock import patch, MagicMock

from pba.patient import Patient
from pba.menu.enqueue_patient import EnqueuePatient


class TestEnqueuePatient(unittest.TestCase):

    def setUp(self):
        self.patient_records = MagicMock()
        self.patient_records.find_patient.return_value = Patient(1234, 'Test Patient', 40, 'Fever')
        self.emergency_queue = MagicMock()
        self.emergency_queue.enqueue_patient.return_value = True
        self.enqueue_patient_option = EnqueuePatient(self.emergency_queue, self.patient_records)

    @patch('builtins.input', side_effect=['1234'])
    def test_enqueue_patient_success(self, mock_input):
        message = self.enqueue_patient_option.execute()
        self.patient_records.find_patient.assert_called_once()
        self.emergency_queue.enqueue_patient.assert_called_once()
        self.assertEqual(message, 'Patient ID (1234) added to the emergency queue successfully.')

    @patch('builtins.input', side_effect=['1234'])
    def test_enqueue_patient_not_found(self, mock_input):
        self.patient_records.find_patient.return_value = None
        message = self.enqueue_patient_option.execute()
        self.patient_records.find_patient.assert_called_once()
        self.emergency_queue.enqueue_patient.assert_not_called()
        self.assertEqual(message, 'No patient records found for ID (1234)! Cannot add to emergency queue.')

    @patch('builtins.input', side_effect=['1234'])
    def test_enqueue_patient_in_queue(self, mock_input):
        self.emergency_queue.enqueue_patient.return_value = False
        message = self.enqueue_patient_option.execute()
        self.patient_records.find_patient.assert_called_once()
        self.emergency_queue.enqueue_patient.assert_called_once()
        self.assertEqual(message, 'Patient ID (1234) is already in the emergency queue! Cannot add duplicate entries.')

    @patch('builtins.input', side_effect=['Fourty-Four'])
    def test_enqueue_patient_bad_input(self, mock_input):
        with self.assertRaises(ValueError):
            self.enqueue_patient_option.execute()
        self.patient_records.find_patient.assert_not_called()
        self.emergency_queue.enqueue_patient.assert_not_called()
