import pygame

pygame.init()

print('Janela inicial')
pygame.joystick.init()
window = pygame.display.set_mode(size=(640, 480))


print('Loop Janela')
while True:
    # check of all events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit() # Close window
            quit() #end pygame


