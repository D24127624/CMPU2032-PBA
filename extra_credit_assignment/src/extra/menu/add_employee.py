from datetime import date
from ..employee import Employee
from ..service.employee_service import EmployeeService
from .menu_option import MenuOption


class AddEmployee(MenuOption):

    def __init__(self, employee_service: EmployeeService):
        self.employee_service = employee_service

    def __str__(self) -> str:
        return 'Add Employee'

    def execute(self) -> str:
        '''Command-line menu option execution to add an employee to the backend database.'''

        try:
            # create a new employee record
            name = input('\n\nEnter Name: ')
            dob = date.fromisoformat(input('Enter Date-of Birth (yyyy-MM-dd): '))
            department = input('Enter Department: ')
            salary = float(input('Enter Salary: '))
            employee = Employee(None, name, dob, department, salary)
            # insert the employee into the database
            self.employee_service.add_employee(employee)
            return f'Employee ID ({employee.id}) added successfully.'
        except Exception as e:
            return f'New employee records failed to get inserted into the DB! {e}'
