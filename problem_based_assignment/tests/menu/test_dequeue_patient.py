import unittest
from unittest.mock import MagicMock

from pba.patient import Patient
from pba.menu.dequeue_patient import DequeuePatient


class TestDequeuePatient(unittest.TestCase):

    def setUp(self):
        self.emergency_queue = MagicMock()
        self.emergency_queue.dequeue_patient.return_value = Patient(1234, 'Test Patient', 40, 'Fever')
        self.dequeue_patient_option = DequeuePatient(self.emergency_queue)

    def test_dequeue_patient_success(self):
        message = self.dequeue_patient_option.execute()
        self.emergency_queue.dequeue_patient.assert_called_once()
        self.assertEqual(message, 'Now serving next patient: Test Patient (age: 40, condition: Fever)')

    def test_dequeue_patient_empty(self):
        self.emergency_queue.dequeue_patient.return_value = None
        message = self.dequeue_patient_option.execute()
        self.emergency_queue.dequeue_patient.assert_called_once()
        self.assertEqual(message, 'No patients in the emergency queue to serve.')
