from xml.dom.minidom import Entity


class nivel:
    def __init__(self, window, name, game_mode):
        self.window = window
        self.name = name
        self.game_mode = game_mode
        self.Entity_list = list[Entity] = []

    def run(self):
        pass
