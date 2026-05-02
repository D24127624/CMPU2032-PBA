from .main_menu import MainMenu
from .menu_option import MenuOption

class MenuBuilder:

    def __init__(self):
        self.__menu_options = {}
        self.__title = 'Main System Menu'
        self.__test_mode = False

    def with_menu_option(self, option: MenuOption | str, key: int = None):
        key = key if key is not None else len(self.__menu_options) + 1
        self.__menu_options[key] = option
        return self

    def with_title(self, title: str):
        self.__title = title
        return self

    def with_test_mode(self):
        self.__test_mode = True
        return self

    def build(self) -> MainMenu:
        if len(self.__menu_options) == 0:
            raise ValueError("At least one menu option must be added.")

        return MainMenu(
            title=self.__title,
            menu_options=dict(sorted(self.__menu_options.items())),
            test_mode=self.__test_mode
        )
