class Coffee:
    def __init__(self, roast, size, ice, temperature, price):
        self.roast = roast
        self.size = size
        self.ice = ice
        self.temperature = temperature
        self.price = price

    def is_hot(self, current_temperature, contains_ice):
        """tells you if your coffee is too cold unless iced"""
        if contains_ice is False:
            if current_temperature > 100:
                return self.temperature == 'warm'
            else:
                return self.temperature == 'not warm'

    def calculate_price(self):
        if self.size == 'large':
            return self.price * 1.5


my_coffee = Coffee('americano', 'large', True, 40, 3.50)
my_price = my_coffee.calculate_price()
print(my_price)
