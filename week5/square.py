from rectangle import Rectangle

class Square(Rectangle):
    def __init__(self, name, side):
        super().__init__(name, side, side)
        self._shape_type = "Square"
    
    @property
    def side(self):
        return self.width  # since width and height are the same for a square

    @side.setter
    def side(self, value):
        if value <= 0:
            raise ValueError("Side must be positive")
        self.width = value
        self.height = value

if __name__ == '__main__':
    try:
        s = int(input("Enter side length: "))
        square = Square("MySquare", s)
        print(square)

        s = int(input("Enter new side length: "))
        square.side = s
        print(square)
    except ValueError as e:
        print(f"Error: {e}")