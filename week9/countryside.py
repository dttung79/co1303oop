from highschool import HighSchoolStudent

class CountrysideStudent(HighSchoolStudent):
    def __init__(self, name, age, avg_grade, addition):
        super().__init__(name, age, avg_grade) # call the parent class constructor
        self.addition = addition

    @property
    def addition(self):
        return self.__addition
    
    @addition.setter
    def addition(self, value):
        if value < 0 or value > 20:
            raise ValueError("Addition must be between 0 and 20")
        self.__addition = value

    def __str__(self):
        return super().__str__() + f', Addition: {self.addition}'
    
    def is_accepted(self, accept_grade):
        return self.avg_grade + self.addition >= accept_grade