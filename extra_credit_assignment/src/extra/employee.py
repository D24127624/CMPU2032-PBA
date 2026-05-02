from datetime import date


class Employee:
    def __init__(self, id: int, name: str, dob: date, department: str, salary: float):
        self.id = id # unique records identifier (can be blank for new records)
        self.name = name
        if not isinstance(dob, date):
            raise TypeError('Invalid type provided for DOB, must be a date.')
        self.dob = dob
        self.department = department
        if not isinstance(salary, float):
            raise TypeError('Invalid type provided for SALARY, must be a float.')
        self.salary = salary

    def __str__(self):
        '''Override the default to-string method to return a human-readable string.'''
        return f'Employee(ID={self.id}, name={self.name}, age={self.dob.isoformat()}, department={self.department}, salary={self.salary})'
