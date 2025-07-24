from my_functions import add, convert

def test_add_01():
    a = 6
    b = 3
    expected = 9
    actual = add(a, b)
    assert actual == expected

def test_add_02():
    a = 6
    b = 0
    expected = 6
    actual = add(a, b)
    assert actual == expected

def test_add_03():
    a = 6
    b = -3
    expected = 3
    actual = add(a, b)
    assert actual == expected


def test_convert_01():
    n = 5
    c = '*'
    expected = '*****'
    actual = convert(n, c)
    assert actual == expected

def test_convert_02():
    n = 6
    c = '+'
    expected = '++++++'
    actual = convert(n, c)
    assert actual == expected

def test_convert_03():
    n = 30
    c = '*'
    expected = '*************************'
    actual = convert(n, c)
    assert actual == expected

def test_convert_04():
    n = 26
    c = '*'
    expected = '*************************'
    actual = convert(n, c)
    assert actual == expected

def test_convert_05():
    n = 25
    c = '*'
    expected = '*************************'
    actual = convert(n, c)
    assert actual == expected

def test_convert_06():
    n = 24
    c = '*'
    expected = '************************'
    actual = convert(n, c)
    assert actual == expected

def test_convert_07():
    n = -10
    c = '*'
    expected = 'Error'
    actual = convert(n, c)
    assert actual == expected

def test_convert_08():
    n = 0
    c = '*'
    expected = ''
    actual = convert(n, c)
    assert actual == expected

def test_convert_09():
    n = -1
    c = '*'
    expected = 'Error'
    actual = convert(n, c)
    assert actual == expected

def test_convert_10():
    n = 1
    c = '*'
    expected = '*'
    actual = convert(n, c)
    assert actual == expected

def test_convert_11():
    n = 5
    c = ''
    expected = 'Error'
    actual = convert(n, c)
    assert actual == expected

def test_convert_12():
    n = 5
    c = '++'
    expected = 'Error'
    actual = convert(n, c)
    assert actual == expected