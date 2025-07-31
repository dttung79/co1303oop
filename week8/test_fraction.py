from fraction import Fraction

def test_str_01():
    f = Fraction(1, 2)
    assert str(f) == "1/2"

def test_str_02():
    f = Fraction(5, 2)
    assert str(f) == "5/2"

def test_str_03():
    f = Fraction(-1, 2)
    assert str(f) == "-1/2"

def test_str_04():
    f = Fraction(1, -2)
    assert str(f) == "-1/2"

def test_str_05():
    f = Fraction(-1, -2)
    assert str(f) == "-1/-2"

def test_denominator():
    try:
        f = Fraction(1, 0)
        assert False
    except ZeroDivisionError as e:
        assert str(e) == "Denominator cannot be zero"