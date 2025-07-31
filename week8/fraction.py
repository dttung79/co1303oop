class Fraction:
    def __init__(self, n, d):
        self.numerator = n
        self.denominator = d

    def __str__(self):
        if self.denominator < 0 and self.numerator > 0:
            return f'-{self.numerator}/{-self.denominator}'
        return f'{self.numerator}/{self.denominator}'

    @property
    def numerator(self):
        return self._numerator
    
    @numerator.setter
    def numerator(self, value):
        self._numerator = value

    @property
    def denominator(self):
        return self._denominator
    
    @denominator.setter
    def denominator(self, value):
        if value == 0:
            raise ZeroDivisionError('Denominator cannot be zero')
        self._denominator = value