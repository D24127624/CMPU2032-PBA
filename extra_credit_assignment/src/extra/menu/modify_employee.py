from datetime import date
from ..employee import Employee
from ..service.employee_service import EmployeeService
from .menu_option import MenuOption


class ModifyEmployee(MenuOption):

    def __init__(self, employee_service: EmployeeService):
        self.employee_service = employee_service

    def __str__(self) -> str:
        return 'Update an employee record'

    def execute(self) -> str:
        '''Command-line menu option execution to update an employee to the backend database.'''

        try:
            employee_id = int(input('\n\nEnter Employee ID: '))
            # create a new employee instance and add it to the employee records
            employee = self.employee_service.search_employee(employee_id)
            if employee:
                name = input(f'Enter Name [{employee.name}]: ') or employee.name
                dob = input(f'Enter Date-of Birth (yyyy-MM-dd) [{employee.dob.isoformat()}]: ') or employee.dob.isoformat()
                department = input(f'Enter Department [{employee.department}]: ') or employee.department
                salary = input(f'Enter Salary [{employee.salary}]: ') or str(employee.salary)
                employee = Employee(employee_id, name, date.fromisoformat(dob), department, float(salary))
                self.employee_service.modify_employee(employee)
                return f'Employee ID ({employee.id}) updated successfully.'
            else:
                return f'Employee ID ({employee_id}) not found.'
        except Exception as e:
            return f'Failed to successfully update the employee ({employee_id}) record! {e}'
