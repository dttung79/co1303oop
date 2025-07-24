def add(a, b):
    c = a + b
    return c

def convert(n, c):
    if n < 0:
        return 'Error'
    
    if len(c) != 1:
        return 'Error'
    
    if n < 25:
        return c * n
    
    return c * 25