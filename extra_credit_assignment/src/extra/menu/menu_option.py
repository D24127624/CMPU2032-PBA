from abc import abstractmethod

class MenuOption:
    '''An interface for a command-line menu option.'''

    @abstractmethod
    def execute(self) -> str:
        '''Executes the menu option's action.'''
        raise NotImplementedError('No implementation found for the execute() method.')
