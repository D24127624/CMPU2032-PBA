from ..repository.employee_db import EmployeeDatabase
from ..employee import Employee


class EmployeeService:
    '''Service layer for employee operations providing access to the EmployeeDatabase repository.'''

    def __init__(self, db: EmployeeDatabase):
        self.db = db

    def initialize_database(self) -> bool:
        '''Creates the employees table in the database.'''
        return self.db.create_table()

    def add_employee(self, employee: Employee) -> Employee:
        '''Creates a new employee record in the database.'''
        return self.db.create_employee(employee)

    def get_all_employees(self) -> list[Employee]:
        '''Retrieves all employee records from the database.'''
        return self.db.read_employees()

    def modify_employee(self, employee: Employee) -> bool:
        '''Updates an existing employee record in the database.'''
        return self.db.update_employee(employee)

    def remove_employee(self, employee_id: int) -> Employee | None:
        '''Removes an employee record from the database by ID.'''
        return self.db.delete_employee(employee_id)

    def search_employee(self, employee_id: int) -> Employee | None:
        '''Removes an employee record from the database by ID.'''
        return self.db.read_employee_by_id(employee_id)
