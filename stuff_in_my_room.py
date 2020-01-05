existence = True


class Walls:
    def __init__(self, color, material):
        self.color = color
        self.material = material


class Desk:
    def __init__(self, number_of_drawers, contents, color, material, physical_state):
        self.number_of_drawers = number_of_drawers
        self.contents = contents
        self.color = color
        self.material = material
        self.physical_state = physical_state

    def atmospheric_pressure(self, pressure):
        if pressure > 100:
            Desk.existence = False
            self.physical_state = 'crumpled'
        return print(self.physical_state)


Walls('light blue', 'drywall')
my_desk = Desk(5, ('paper', 'pencil', 'books', 'soda'), 'white', 'wood', 'normal')
current_pressure = int(input())
Desk.atmospheric_pressure(my_desk, current_pressure)

