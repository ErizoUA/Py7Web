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
    def __init__(self, floor: Floor, ceiling: Ceiling, walls: Wall):
        self.floor = floor
        self.ceiling = ceiling
        self.walls = walls


if __name__ == '__main__':

    house = Building(Floor(), Ceiling(), Wall())

    house.floor.build()
    house.walls.build()
    house.ceiling.build()
