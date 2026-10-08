import pygame

from code.Menu import Menu


class game:
    def __init__(self):
        pygame.joystick.init()
        self.window = pygame.display.set_mode(size=(640, 480))

    def run(self):
        while True:
            menu = Menu(self.window)
            menu.run()
            pass


            # check of all events
            #for event in pygame.event.get():
             #   if event.type == pygame.QUIT:
              #      pygame.quit()  # Close window
               #     quit()  # end pygame




