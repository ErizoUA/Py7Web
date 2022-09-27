class Floor:
    def __init__(self):
        self.name = 'floor'

    def build(self):
        print(f'Build: {self.name}')


class Ceiling:
    def __init__(self):
        self.name = 'ceiling'

    def build(self):
        print(f'Build: {self.name}')


class Wall:
    def __init__(self):
        self.name = 'walls'

    def build(self):
        print(f'Build: {self.name}')


class Building:
    def __init__(self):
        self.floor = None
        self.ceiling = None
        self.walls = None

    def inject_floor(self, floor: Floor):
        self.floor = floor

    def inject_ceiling(self, ceiling: Ceiling):
        self.ceiling = ceiling

    def inject_walls(self, walls: Wall):
        self.walls = walls


def build():  # Fabric
    house = Building()
    house.inject_floor(Floor())
    house.inject_walls(Wall())
    house.inject_ceiling(Ceiling())
    return house


if __name__ == '__main__':
    
    house = build()

    house.floor.build()
    house.walls.build()
    house.ceiling.build()
    