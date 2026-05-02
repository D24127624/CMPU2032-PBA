class Patient:
    def __init__(self, id: int, name: str, age:int, condition: str):
        if not isinstance(id, int):
            raise TypeError('Invalid type provided for ID, must be an integer.')
        self.id = id
        self.name = name
        if not isinstance(age, int):
            raise TypeError('Invalid type provided for AGE, must be an integer.')
        self.age = age
        self.condition = condition

    def __str__(self):
        '''Override the default to-string method to return a human-readable string.'''
        return f'Patient(ID={self.id}, name={self.name}, age={self.age}, condition={self.condition})'
