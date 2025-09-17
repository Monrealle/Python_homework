def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return abs(a)
    
    
assert gcd(-15, 3) == 3