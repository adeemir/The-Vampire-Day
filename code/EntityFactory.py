from code.Background import Background


class EntityFactory:

    @staticmethod
    def get_entity(entity_name: str, position=(0, 0)):
        match entity_name:
            case'level1':
                list_bg = []
                for i in range(1,3):
                    list_bg.append(Background(f'level{i}', position))
                    pass
                return list_bg
        return[]



