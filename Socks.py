class Socks:
    def __init__(self, color, size, fabric, brand, style):
        self.color = color
        self.size = size
        self.fabric = fabric
        self.brand = brand
        self.style = style

    def is_soft(fabric):
        types_of_fabric = ['wool', 'cotton', 'cashmere']
        if fabric in types_of_fabric:
            return print('your socks are soft')
        else:
            return print('your socks are NOT soft')


my_sock = Socks('red', 10, 'polyester', 'Nike', 'tube')
print(vars(my_sock))
Socks.is_soft('polyester')