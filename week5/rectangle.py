from shape import Shape

class Rectangle(Shape):
    def __init__(self, name, width, height):
        super().__init__(name)  # call the base class constructor
        self._shape_type = "Rectangle"  # set the shape type
        self.width = width
        self.height = height

    @property
    def width(self):
        return self._width
    
    @width.setter
    def width(self, value):
        if value <= 0:
            raise ValueError("Width must be positive")
        self._width = value

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, value):
        if value <= 0:
            raise ValueError("Height must be positive")
        self._height = value

    # override area property of Shape class
    @property
    def area(self):
        return self.width * self.height
    
    # override __str__ method of Shape class
    def __str__(self):
        shape_info = super().__str__()
        rect_info = shape_info + f' ({self.width}cm x {self.height}cm)'
        return rect_info

### Test the Rectangle class
if __name__ == '__main__':
    try:
        w = int(input("Enter width: "))
        h = int(input("Enter height: "))
        r = Rectangle("ABCD", w, h)
        print(r)
    except ValueError as e:
        print(f"Error: {e}")