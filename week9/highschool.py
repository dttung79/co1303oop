class HighSchoolStudent:
    def __init__(self, name, age, avg_grade):
        self.name = name
        self.age = age
        self.avg_grade = avg_grade

    @property
    def name(self):
        return self._name # protected attribute

    @property
    def age(self):
        return self._age # protected attribute

    @property
    def avg_grade(self):
        return self._avg_grade # protected attribute
    
    @name.setter
    def name(self, value):
        if value == '':
            raise ValueError("Name cannot be empty")
        self._name = value

    @age.setter
    def age(self, value):
        if value <= 0:
            raise ValueError("Age must be positive")
        self._age = value

    @avg_grade.setter
    def avg_grade(self, value):
        if not (0 <= value <= 100):
            raise ValueError("Average grade must be between 0 and 100")
        self._avg_grade = value

    def __str__(self):
        info = f'Name: {self.name}, Age: {self.age}, Average Grade: {self.avg_grade}'
        return info
    
    def is_accepted(self, accept_grade):
        return self.avg_grade >= accept_grade