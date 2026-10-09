import pygame

from code.Menu import Menu
from code.Window import WIN_WIDTH, WIN_HEIGHT


class game:
    def __init__(self):
        pygame.init()
        pygame.joystick.init()
        pygame.mixer.init()
        self.window = pygame.display.set_mode(size=(WIN_WIDTH, WIN_HEIGHT))

    def run(self):


        while True:
            menu = Menu(self.window)
            menu.run()
            pass







