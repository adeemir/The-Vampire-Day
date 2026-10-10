import pygame

from code.Menu import Menu
from code.Nivel import nivel
from code.Window import WIN_WIDTH, WIN_HEIGHT, MENU_OPTION


class game:
    def __init__(self):
        pygame.init()
        pygame.joystick.init()
        pygame.mixer.init()
        self.window = pygame.display.set_mode(size=(WIN_WIDTH, WIN_HEIGHT))

    def run(self):


        while True:
            menu = Menu(self.window)
            menu_return = menu.run()

            if menu_return in [MENU_OPTION[0], MENU_OPTION[1], MENU_OPTION[2]]:
                Nivel = nivel(self.window, 'Nível1', menu_return)
                Nivel.run()
            elif menu_return == MENU_OPTION[3]:
                pygame.quit()
                quit()
            else:
                pass










