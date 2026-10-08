import pygame

from code.Menu import Menu


class game:
    def __init__(self):
        pygame.joystick.init()
        pygame.mixer.init()
        self.window = pygame.display.set_mode(size=(576, 324))

    def run(self):


        while True:
            menu = Menu(self.window)
            menu.run()
            pass







