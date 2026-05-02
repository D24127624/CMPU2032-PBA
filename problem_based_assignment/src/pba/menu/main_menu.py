import os
import re

from .menu_option import MenuOption


class MainMenu:

    def __init__(self, title: str, menu_options: dict[int, MenuOption | str], test_mode: bool = False):
        self.title = title
        self.menu_options = menu_options
        self.test_mode = test_mode
        self.show_full_menu = True

    def display_menu(self, message: str):
        '''Displays the menu options to the user.'''

        # clean the screen before displaying the message & menu
        if self.test_mode == False:
            os.system('clear' if os.name != 'nt' else 'cls')

        # display the message, if provided
        if message:
            print(f'\n{message}\n')
        # display the system menu
        print(f'\n===== {self.title} =====')
        if(self.show_full_menu):
            for key, value in self.menu_options.items():
                prefix = ' ' if key < 10 else ''
                print(f'{prefix}{key}. {value}')
        else:
            print('0. Redisplay Full Menu')
        self.show_full_menu = False

    def run(self):
        '''Launch the command-line menu and handle top-level menu input.'''

        message = ''
        # main-menu loop until the user chooses to exit the program
        while True:
            # display the menu options and prompt the user for input
            self.display_menu(message)
            choice = input('\nEnter your choice: ')
            # redisplay the full menu
            if self.show_full_menu == False and choice == '0':
                print('fm')
                self.show_full_menu = True
            # exit the program
            elif choice == '10':
                print(f'\n\nExiting the {self.title}... Goodbye!\n\n')
                break
            # validate the user has provided a valid input
            elif re.match(r'^([1-9])$', choice) is None:
                self.show_full_menu = True
                message = 'Invalid choice. Please enter a number between 1 and 10.'
            # execute the menu option chosen by the user
            else:
                message = self.menu_options[int(choice)].execute()
