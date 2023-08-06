"""
Test file.
"""
import random
import pygame
import pygame_menu

pygame.init()
screen = pygame.display.set_mode((640, 480))
theme = pygame_menu.themes.THEME_BLUE.copy()
theme.widget_margin = (0, 5)
menu = pygame_menu.Menu('Button disable', 640, 480, theme=theme)


def check_name(name_value: str = '') -> None:
    """
    Checks the name, which updates the button.
    For complex mechanisms, you can use a class to store the name variable
    instead of accesing global ones (like this case).

    :param name_value: Value passed from onchange() text input method
    """
    global button
    name_ready = name_value != ''
    print('User not configured yet' if not name_ready else 'User ready!')
    button.readonly = not name_ready
    button.set_selection_effect(None if not name_ready else theme.widget_selection_effect)


def game() -> None:
    """
    Starts the game, this method only changes the background color of the menu.
    """
    print('Game started!')
    menu.get_scrollarea().update_area_color((random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)))


# Create a basic input
name = menu.add.text_input('Enter your name: ', onchange=check_name)
button = menu.add.button('Play', game)
menu.add.button('Exit', pygame_menu.events.EXIT)

# Call start game to setup the initial status, it retrieves the name (which is empty at the app start),
# and disables the button by setting readonly, also dynamically updates the selection effect
check_name()
menu.mainloop(surface=screen)
