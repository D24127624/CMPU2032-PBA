import unittest

from pba.patient import Patient
from pba.emergency_queue import EmergencyQueue


class TestEmergencyQueue(unittest.TestCase):

    def setUp(self):
        self.patient1 = Patient(1234, 'Patient One', 36, 'Nausea')
        self.patient2 = Patient(5678, 'Patient Two', 40, 'Fever')
        self.patient3 = Patient(9876, 'Patient Three', 52, 'Cold')
        self.emergency_queue = EmergencyQueue()

    def test_enqueue_patient_success(self):
        self.assertTrue(self.emergency_queue.is_empty())
        self.emergency_queue.enqueue_patient(self.patient1)
        self.assertFalse(self.emergency_queue.is_empty())
        self.emergency_queue.enqueue_patient(self.patient2)
        self.assertEqual(len(self.emergency_queue.view_queue()), 2)
        self.emergency_queue.enqueue_patient(self.patient3)
        self.assertEqual(len(self.emergency_queue.view_queue()), 3)

    def test_enqueue_patient_duplicate(self):
        self.assertTrue(self.emergency_queue.is_empty())
        self.assertTrue(self.emergency_queue.enqueue_patient(self.patient1))
        self.assertFalse(self.emergency_queue.is_empty())
        self.assertFalse(self.emergency_queue.enqueue_patient(self.patient1))
        self.assertTrue(self.emergency_queue.enqueue_patient(self.patient2))
        self.assertFalse(self.emergency_queue.enqueue_patient(self.patient2))

    def test_dequeue_patient_success(self):
        self.assertIsNone(self.emergency_queue.dequeue_patient())
        self.emergency_queue.enqueue_patient(self.patient2)
        self.emergency_queue.enqueue_patient(self.patient3)
        self.emergency_queue.enqueue_patient(self.patient1)
        self.assertEqual(len(self.emergency_queue.view_queue()), 3)
        self.assertEqual(self.emergency_queue.dequeue_patient(), self.patient2)
        self.assertEqual(self.emergency_queue.dequeue_patient(), self.patient3)
        self.assertEqual(self.emergency_queue.dequeue_patient(), self.patient1)
        self.assertTrue(self.emergency_queue.is_empty())
