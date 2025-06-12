from fruit import Fruit

class FruitMart:
    def __init__(self, name):
        self.__name = name
        self.__fruits = []  # empty list of fruits
        self.__total_sale = 0

    @property
    def total_sale(self):
        return self.__total_sale

    @property
    def name(self):
        return self.__name
    
    @name.setter
    def name(self, new_name):
        if new_name == '':
            print('Invalid name')
            return
        
        self.__name = new_name
    
    def import_fruit(self, fruit, quantity):
        if fruit in self.__fruits:
            fruit.quantity += quantity
        else:
            fruit.quantity = quantity
            self.__fruits.append(fruit)
    
    def sell(self, fruit, quantity):
        if fruit not in self.__fruits:
            print(f'{fruit.name} does not exist')
            return
        
        if quantity > fruit.quantity:
            print(f'Not enough quantity. Max quantity is {fruit.quantity}')
            return
        
        fruit.quantity -= quantity
        self.__total_sale += quantity * fruit.price

        print(f'Sell {quantity} {fruit.name}. In stock: {fruit.quantity}')

    def get_fruit(self, number):
        if number < 0 or number >= len(self.__fruits):
            print('Invalid number!')
            return None
        
        return self.__fruits[number]
    
    def show_fruits(self):
        print(f'All fruits in mart {self.__name}:')
        for i in range(len(self.__fruits)):
            print(f'{i + 1}. ', end='')
            self.__fruits[i].show()

## Test ##
if __name__ == '__main__':
    apple = Fruit('apple', 0, 2)
    banana = Fruit('banana', 0, 1.5)
    mango = Fruit('mango', 0, 2.5)

    winmart = FruitMart('Winmart')
    winmart.import_fruit(apple, 100)
    winmart.import_fruit(banana, 200)
    winmart.import_fruit(mango, 150)

    winmart.show_fruits()