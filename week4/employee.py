class Employee:
    # class attributes
    _id_count = 0
    _BASIC_SALARY = 1000
    def __init__(self, name, rate):
        self.name = name
        self.rate = rate
        # increase class attribute everytime an object is created
        Employee._id_count += 1
        # instance attribute (or object attribute)
        self._emp_id = Employee._id_count

        # debug
        #print(f'Number of employees created: {Employee._id_count}')

    # provide get property only because ID cannot be changed
    @property
    def emp_id(self):
        return self._emp_id 
    
    @property
    def name(self):
        return self._name   # protected object attribute
    
    @name.setter
    def name(self, new_name):
        if new_name == '':
            raise ValueError('Error: Name cannot be empty!')
        
        self._name = new_name

    # TODO: write getter, setter for rate (0 < rate <= 10)
    @property
    def rate(self):
        return self._rate
    
    @rate.setter
    def rate(self, new_rate):
        if new_rate <= 0 or new_rate > 10:
            raise ValueError('Error: rate is out of range')
        
        self._rate = new_rate

    @property
    def salary(self):
        return self.rate * Employee._BASIC_SALARY

    def __str__(self):
        return f'ID: {self.emp_id}, name: {self.name}, salary: ${self.salary}'

### Test Employee ###
if __name__ == '__main__':
    john = Employee('John', 1.0)
    paul = Employee('Paul', 1.5)

    print(john.emp_id)
    print(paul.emp_id)

    #mike = Employee('', 1.1)
    paul.name = 'Paula'
    print(paul.name)

    #mike = Employee('Mike', 0) # error
    #mike = Employee('Mike', 11) # error

    paul.rate = 2.0
    print(paul.salary)

    print(john)
    print(paul)
