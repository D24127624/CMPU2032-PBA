from ..service.employee_service import EmployeeService
from .menu_option import MenuOption


class GetAllEmployees(MenuOption):

    def __init__(self, employee_service: EmployeeService):
        self.employee_service = employee_service

    def __str__(self) -> str:
        return 'Display all employee records'

    def execute(self):
        '''Command-line menu option execution to display all available employee records.'''

        employees = self.employee_service.get_all_employees()
        if employees:
            message = f'{'ID':<5} {'Name':<20} {'DOB':<10} {'Department':<20} {'Salary':<10}'
            message += '\n' + ('-' * 75)
            for employee in employees:
                message += f'\n{employee.id:<5} {employee.name:<20} {employee.dob.isoformat():<10} {employee.department:<20} {employee.salary:<10}'
        else:
            message = 'No employee records found.'
        return message
