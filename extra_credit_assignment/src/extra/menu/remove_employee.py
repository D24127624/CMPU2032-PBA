from ..service.employee_service import EmployeeService
from .menu_option import MenuOption


class RemoveEmployee(MenuOption):

    def __init__(self, employee_service: EmployeeService):
        self.employee_service = employee_service

    def __str__(self) -> str:
        return 'Remove Employee'

    def execute(self) -> str:
        '''Command-line menu option execution to remove an employee from the backend database.'''

        try:
            employee_id = int(input('\n\nEnter Employee ID: '))
            # create a new employee instance and add it to the employee records
            employee = self.employee_service.search_employee(employee_id)
            if employee:
                self.employee_service.remove_employee(employee.id)
                return f'Employee ID ({employee.id}) removed successfully.'
            else:
                return f'Employee ID ({employee_id}) not found.'
        except Exception as e:
            return f'Failed to successfully remove the employee ({employee_id}) record! {e}'
