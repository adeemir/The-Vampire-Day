from xml.dom.minidom import Entity

import pygame

from code.EntityFactory import EntityFactory


class nivel:
    def __init__(self, window, name, game_mode):
        self.entity_list = None
        self.window = window
        self.name = name
        self.game_mode = game_mode
        self.entity_list: list[Entity] = []
        self.entity_list.extend(EntityFactory.get_entity('level1'))

    def run(self):
        while True:
            for ent in self.entity_list:
                self.window.blit(source=ent.surf, dest=ent.rect)
            pygame.display.flip()
            pass
