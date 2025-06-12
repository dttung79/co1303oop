from fruit import Fruit
from fruit_mart import FruitMart

class MartManager:
    def __init__(self, mart_name):
        self.__mart = FruitMart(mart_name)
        self.import_fruits()    # import some default fruits
    
    def import_fruits(self):
        apple = Fruit('apple', 0, 2)
        banana = Fruit('banana', 0, 1.5)
        mango = Fruit('mango', 0, 2.5)

    
        self.__mart.import_fruit(apple, 100)
        self.__mart.import_fruit(banana, 200)
        self.__mart.import_fruit(mango, 150)

    def run(self):
        running = True
        while running:
            self.print_menu()
            choice = int(input('Enter your choice: '))
            if choice == 1:
                self.show_fruits()
            elif choice == 2:
                self.import_fruit() # import 1 fruit entered by user
            elif choice == 3:
                self.sell_fruit()
            elif choice == 4:
                self.show_sale()
            elif choice == 5:
                print('Exit.')
                running = False
            else:
                print('Invalid choice!')
    
    def print_menu(self):
        print(f'Welcome to {self.__mart.name}') # call property name of FruitMart
        print('-----------------------------------------')
        print('1. Show fruits')
        print('2. Import fruit')
        print('3. Sell fruit')
        print('4. Show total sale')
        print('5. Exit')
    
    def show_fruits(self):
        self.__mart.show_fruits()
    
    def import_fruit(self):
        choice = input('Import new fruit or current fruit? (new/current): ')
        if choice == 'new':
            self.import_new_fruit()
        elif choice == 'current':
            self.import_current_fruit()
        else:
            print('Invalid answer')

    def import_new_fruit(self):
        name = input('Enter fruit name: ')
        quantity = int(input('Enter quantity: '))
        price = float(input('Enter price: '))

        fruit = Fruit(name, quantity, price)
        self.__mart.import_fruit(fruit, quantity)

    def import_current_fruit(self):
        number = int(input('Enter fruit number: '))
        fruit = self.__mart.get_fruit(number - 1)
        quantity = int(input('Enter imported quantity: '))

        self.__mart.import_fruit(fruit, quantity)

    def sell_fruit(self):
        number = int(input('Enter fruit number: '))
        fruit = self.__mart.get_fruit(number - 1)
        quantity = int(input('Enter quantity to sell: '))

        self.__mart.sell(fruit, quantity)

    def show_sale(self):
        print(f'Total sale: ${self.__mart.total_sale}')

#### MAIN PROGRAM ####
program = MartManager('Winmart')
program.run()