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
            print('Invalid fruit name!')
            return
        
        self.__name = new_name

    @property
    def quantity(self):
        return self.__quantity
    
    @quantity.setter
    def quantity(self, new_quantity):
        if new_quantity < 0:
            print('Invalid quantity!')
            return
        
        self.__quantity = new_quantity

    @property
    def price(self):
        return self.__price
    
    @price.setter
    def price(self, new_price):
        if new_price <= 0:
            print('Invalid price!')
            return
        
        self.__price = new_price

    def show(self):
        print(f'{self.__name}, quantity: {self.__quantity}, price: ${self.__price}')