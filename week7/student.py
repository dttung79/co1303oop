# Create your own exception
class GPAValueError(ValueError):
    def __init__(self, message="GPA must be a float between 0.0 and 5.0."):
        self.message = message
        super().__init__(self.message)

class NameValueError(ValueError):
    def __init__(self, message="Name must be a non-empty string."):
        self.message = message
        super().__init__(self.message)

class AgeValueError(ValueError):
    def __init__(self, message="Age must be a non-negative integer."):
        self.message = message
        super().__init__(self.message)

class Student:
    def __init__(self, name, age, gpa):
        self.name = name
        self.age = age
        self.gpa = gpa
    
    @property
    def name(self):
        return self.__name
    
    @name.setter
    def name(self, new_name):
        if not isinstance(new_name, str) or new_name == '':
            raise NameValueError("Name must be a non-empty string.")
        self.__name = new_name
    
    @property
    def age(self):
        return self.__age
    
    @age.setter
    def age(self, new_age):
        if not isinstance(new_age, int) or new_age < 0:
            raise AgeValueError("Age must be a non-negative integer.")
        self.__age = new_age

    @property
    def gpa(self):
        return self.__gpa
    
    @gpa.setter
    def gpa(self, new_gpa):
        if not isinstance(new_gpa, float) or new_gpa < 0.0 or new_gpa > 5.0:
            raise GPAValueError("GPA must be a float between 0.0 and 5.0.")
        self.__gpa = new_gpa