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


def build():  # Fabric
    house = Building()
    house.floor = Floor()
    house.walls = Wall()
    house.ceiling = Ceiling()
    return house


if __name__ == '__main__':
    
    house = build()

    house.floor.build()
    house.walls.build()
    house.ceiling.build()
