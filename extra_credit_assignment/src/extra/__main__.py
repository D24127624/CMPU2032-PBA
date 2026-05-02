from .menu.menu_builder import MenuBuilder
from .menu.add_employee import AddEmployee
from .menu.get_all_employees import GetAllEmployees
from .menu.modify_employee import ModifyEmployee
from .menu.remove_employee import RemoveEmployee

from .repository.impl.sqlite_employee_db import SqliteEmployeeDatabase
from .service.employee_service import EmployeeService


def main():
    # initialize the database and service layers
    employee_db = SqliteEmployeeDatabase('ems.db')
    employee_db.initialize_database()
    employee_service = EmployeeService(employee_db)

    menu_builder = (
        MenuBuilder()
        .with_title('Employee Management System')
        .with_menu_option(AddEmployee(employee_service))
        .with_menu_option(GetAllEmployees(employee_service))
        .with_menu_option(ModifyEmployee(employee_service))
        .with_menu_option(RemoveEmployee(employee_service))
        .with_menu_option('Exit', 10)
    )
    menu_builder.build().run()


if __name__ == '__main__':
    main()
