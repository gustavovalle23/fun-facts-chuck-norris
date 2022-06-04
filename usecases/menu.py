from typing import Dict, Any

from core.checks.database_checks import initial_check
from core.common import clear_screen
from core.errors import option_not_found
from core.messages import *
from usecases.about import about
from usecases.authentication import login, register
from usecases.show_car import show_cars

initial_choices: Dict[str, Any] = {
    "1": login,
    "2": register,
    "3": about,
    "0": exit
}


def initial_menu():
    """ show menu with login, register, logout and exit options """
    clear_screen()
    initial_check()
    print(welcome_message)
    option: str = input("\n Type your choice: ")
    initial_choices.get(option, option_not_found)()


def features_menu():
    clear_screen()
    print(features_menu_message)
    option: str = input("\n Type your choice: ")
    show_cars(option)
