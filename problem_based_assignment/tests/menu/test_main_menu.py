import unittest
from unittest.mock import patch, MagicMock

from pba.menu.add_patient import AddPatient
from pba.menu.dequeue_patient import DequeuePatient
from pba.menu.menu_builder import MenuBuilder
from pba.menu.view_records import ViewRecords
from pba.patient import Patient


class TestMainMenu(unittest.TestCase):

    def setUp(self):
        patient1 = Patient(1234, 'Patient One', 36, 'Nausea')
        patient2 = Patient(5678, 'Patient Two', 40, 'Fever')
        self.patient_records = MagicMock()
        self.patient_records.next_id.return_value = 1234
        self.patient_records.find_patient.return_value = patient1
        self.patient_records.list_patients.return_value = [patient1, patient2]
        self.emergency_queue = MagicMock()
        self.emergency_queue.dequeue_patient.return_value = patient2
        self.main_menu = (
            MenuBuilder()
            .with_menu_option(AddPatient(self.patient_records), 1)
            .with_menu_option(ViewRecords(self.patient_records), 2)
            .with_menu_option(DequeuePatient(self.emergency_queue), 6)
            .with_menu_option('Exit', 10)
            .with_test_mode()
            .build()
        )

    @patch('builtins.input', side_effect=['1', 'Test Patient', '43', 'Fever', '10'])
    def test_add_patient_flow(self, mock_input):
        self.main_menu.run()
        self.patient_records.add_patient.assert_called_once()

    @patch('builtins.input', side_effect=['6', '10'])
    def test_dequeue_patient_flow(self, mock_input):
        self.main_menu.run()
        self.emergency_queue.dequeue_patient.assert_called_once()

    @patch('builtins.input', side_effect=['2', '10'])
    def test_view_records_flow(self, mock_input):
        self.main_menu.run()
        self.patient_records.list_patients.assert_called_once()
