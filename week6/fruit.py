class Fruit:
    def __init__(self, name, quantity, price):
        self.__name = name
        self.__quantity = quantity
        self.__price = price
    
    @property
    def name(self):
        return self.__name
    
    @name.setter
    def name(self, new_name):
        if new_name == '':
            raise ValueError('Name cannot be empty!')
        
        self.__name = new_name

    @property
    def quantity(self):
        return self.__quantity
    
    @quantity.setter
    def quantity(self, new_quantity):
        if new_quantity < 0:
            raise ValueError('Quantity cannot be negative!')
        
        self.__quantity = new_quantity

    @property
    def price(self):
        return self.__price
    
    @price.setter
    def price(self, new_price):
        if new_price <= 0:
            raise ValueError('Price must be greater than zero!')
        
        self.__price = new_price

    def __str__(self):
        return f'{self.__name}, quantity={self.__quantity}, price=${self.__price}'