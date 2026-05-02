import sqlite3

from datetime import date
from ...employee import Employee
from ..employee_db import EmployeeDatabase


class SqliteEmployeeDatabase(EmployeeDatabase):
    '''SQLite implementation of the Employee-Database repository.'''

    def __init__(self, db_name='ems.db'):
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()

    def initialize_database(self) -> bool:
        '''Initializes the database by creating any required tables.'''

        sql_query = '''
CREATE TABLE IF NOT EXISTS employees (
    employee_id INTEGER         PRIMARY KEY AUTOINCREMENT,
    name        VARCHAR(255)    NOT NULL,
    dob         DATE            NOT NULL,
    department  VARCHAR(255),
    salary      FLOAT           NOT NULL
)
        '''
        # performs the table creation operation
        with self.conn:
            self.cursor.execute(sql_query)

    def create_employee(self, employee: Employee) -> Employee:
        '''Creates a new employee record in the database.'''

        sql_query = '''
INSERT INTO employees (name, dob, department, salary)
               VALUES (?, ?, ?, ?)
        '''
        # perform the insertion operation
        with self.conn:
            self.cursor.execute(
                sql_query,
                (employee.name,
                employee.dob.isoformat(),
                employee.department,
                employee.salary)
            )
            # update and return employee object
            employee.id = self.cursor.lastrowid
            return employee

    def read_employees(self) -> list[Employee]:
        '''Reads all employee records from the database.'''

        sql_query = '''
SELECT employee_id,
       name,
       dob,
       department,
       salary
  FROM employees
        '''
        # perform the selection operation
        with self.conn:
            self.cursor.execute(sql_query)
            rows = self.cursor.fetchall()
            result = [Employee(row[0], row[1], date.fromisoformat(row[2]), row[3], row[4]) for row in rows]
            return result

    def read_employee_by_id(self, employee_id: int) -> Employee | None:
        '''Reads employee records from the database and filters by the provided ID.'''

        sql_query = '''
SELECT employee_id,
       name,
       dob,
       department,
       salary
  FROM employees
 WHERE employee_id = ?
        '''
        # perform the selection operation
        with self.conn:
            self.cursor.execute(sql_query, (employee_id, ))
            rows = self.cursor.fetchall()
            result = [Employee(row[0], row[1], date.fromisoformat(row[2]), row[3], row[4]) for row in rows]
            return result[0] if len(result) == 1 else None

    def update_employee(self, employee: Employee) -> bool:
        '''Updates an existing employee record in the database.'''

        sql_query = '''
UPDATE employees
   SET name = ?,
       dob = ?,
       department = ?,
       salary = ?
 WHERE employee_id = ?
        '''
        # perform the update operation
        with self.conn:
            self.cursor.execute(
                sql_query,
                (employee.name,
                employee.dob.isoformat(),
                employee.department,
                employee.salary,
                employee.id)
            )
            return self.cursor.rowcount == 1

    def delete_employee(self, employee_id: int) -> Employee | None:
        '''Removes an employee record from the database by its ID.'''

        sql_query = '''
DELETE FROM employees
      WHERE employee_id = ?
        '''
        # perform the update operation
        with self.conn:
            self.cursor.execute(sql_query, (employee_id, ))
            return self.cursor.rowcount == 1
