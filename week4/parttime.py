from employee import Employee

class PartTime(Employee):
    def __init__(self, name, rate, hours):
        super().__init__(name, rate)
        self.hours = hours
    
    # TODO: getter/setter for hours (10 <= hours <= 40)
    @property
    def hours(self):
        return self.__hours
    
    @hours.setter
    def hours(self, new_hours):
        if new_hours < 10 or new_hours > 40:
            raise ValueError('Error: Hours is out of range')
        
        self.__hours = new_hours
    
    # TODO: override salary
    @property
    def salary(self):
        return super().salary * self.hours / 40

    # TODO: override __str__
    def __str__(self):
        return super().__str__() + f', hours: {self.hours}'
    
if __name__ == '__main__':
    john = PartTime('John', 1.0, 20)
    print(john)

    paul = PartTime('Pau', 1.0, 10)
    print(paul)

    #mike = PartTime('Mike', 1.0, 50)    # error