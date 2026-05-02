from abc import ABC, abstractmethod
from ..employee import Employee


class EmployeeDatabase(ABC):
    '''An interface definition used for implementations of the Employee-Database backend.'''

    @abstractmethod
    def initialize_database(self) -> bool:
        '''Initializes the database by creating any required tables.'''
        raise NotImplementedError('No implementation found for the create_table() method.')

    @abstractmethod
    def create_employee(self, employee: Employee) -> Employee:
        '''Creates a new employee record in the database.'''
        raise NotImplementedError('No implementation found for the create_employee(employee) method.')

    @abstractmethod
    def read_employees(self) -> list[Employee]:
        '''Reads all employee records from the database.'''
        raise NotImplementedError('No implementation found for the read_employees() method.')

    @abstractmethod
    def read_employee_by_id(self, employee_id: int) -> Employee | None:
        '''Reads all employee records from the database.'''
        raise NotImplementedError('No implementation found for the read_employees() method.')

    @abstractmethod
    def update_employee(self, employee: Employee) -> bool:
        '''Updates an existing employee record in the database.'''
        raise NotImplementedError('No implementation found for the update_employee(uemployee) method.')

    @abstractmethod
    def delete_employee(self, employee_id: int) -> Employee | None:
        '''Removes an employee record from the database by its ID.'''
        raise NotImplementedError('No implementation found for the delete_employee(employee_id) method.')
