from employee import Employee

class FullTime(Employee):
    def __init__(self, name, rate, insurance):
        # call __init__ from super class (Employee)
        super().__init__(name, rate)
        self.insurance = insurance

    @property
    def insurance(self):
        return self.__insurance
    
    @insurance.setter
    def insurance(self, new_insurance):
        if new_insurance <= 0:
            raise ValueError('Error: insurance must be positive')
        
        self.__insurance = new_insurance
    
    # override __str__ method
    def __str__(self):
        employee_info = super().__str__()
        fulltime_info = employee_info + f', insurance: ${self.insurance}'
        return fulltime_info
    
####
if __name__ == '__main__':
    john = FullTime('John', 1.5, 50)
    print(john)