from abc import ABC, abstractmethod

class Shape(ABC):
    def __init__(self, name):
        self.name = name            # calling the setter for validation  
        self._shape_type = "Shape"  # protected attribute
    
    @property
    def name(self):
        return self._name # protected attribute
    
    @name.setter
    def name(self, new_name):
        if new_name == '':
            raise ValueError("Name cannot be empty")
        
        self._name = new_name

    # provide only getters for shape_type
    @property
    def shape_type(self):
        return self._shape_type
    
    # define an abstract property to calculate area
    # it must be abstract because we don't know how to calculate area in the base class
    @property
    @abstractmethod
    def area(self):
        pass

    def __str__(self):
        return f'{self.shape_type} {self.name}: Area {self.area} cm^2'