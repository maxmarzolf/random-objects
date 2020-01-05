class Socks:
    def __init__(self, color, size, fabric, brand, style):
        self.color = color
        self.size = size
        self.fabric = fabric
        self.brand = brand
        self.style = style

    @staticmethod
    def are_soft(fabric):
        types_of_fabric = ['wool', 'cotton', 'cashmere']
        if fabric in types_of_fabric:
            return print('your socks are soft')
        else:
            return print('your socks are NOT soft')

    @staticmethod
    def number_in_drawer(drawer):
        sock_count = 0
        for _ in drawer:
            sock_count += 1
        return print(f'you have {sock_count} socks in your drawer')


my_sock = Socks('red', 10, 'polyester', 'Nike', 'tube')
print(vars(my_sock))
Socks.are_soft('polyester')
Socks.number_in_drawer(['tube', 'anklet', 'quarter'])
