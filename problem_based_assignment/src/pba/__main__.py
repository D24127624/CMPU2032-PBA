from .patient_records import PatientRecords
from .emergency_queue import EmergencyQueue
from .menu.menu_builder import MenuBuilder
from .menu.add_patient import AddPatient
from .menu.delete_patient import DeletePatient
from .menu.dequeue_patient import DequeuePatient
from .menu.enqueue_patient import EnqueuePatient
from .menu.search_patient import SearchPatient
from .menu.sort_by_age import SortByAge
from .menu.sort_by_id import SortById
from .menu.view_queue import ViewQueue
from .menu.view_records import ViewRecords


def main():
    emergency_queue = EmergencyQueue()
    patient_records = PatientRecords()

    menu_builder = (
        MenuBuilder()
        .with_title('Smart Hospital System')
        .with_menu_option(AddPatient(patient_records))
        .with_menu_option(ViewRecords(patient_records))
        .with_menu_option(DeletePatient(patient_records))
        .with_menu_option(SearchPatient(patient_records))
        .with_menu_option(EnqueuePatient(emergency_queue, patient_records))
        .with_menu_option(DequeuePatient(emergency_queue))
        .with_menu_option(ViewQueue(emergency_queue))
        .with_menu_option(SortById(patient_records))
        .with_menu_option(SortByAge(patient_records))
        .with_menu_option('Exit')
    )
    menu_builder.build().run()


if __name__ == '__main__':
    main()
