def extended_gcd(a, b):
    x, xx = 1, 0  # коэффициенты для a
    y, yy = 0, 1  # коэффициенты для b
    
    while b != 0:
        q = a // b
        a, b = b, a % b 
        
        x, xx = xx, x - q * xx
        y, yy = yy, y - q * yy
    
    return a, x, y # a - НОД, x y - искомые коэффициенты Безу

def main():

    a = int(input("Введите a: "))
    b = int(input("Введите b: "))

    gcd, x, y = extended_gcd(a, b)

    print(f"\nНОД({a}, {b}) = {gcd}")
    print(f"Коэффициенты: x = {x}, y = {y}")

if __name__ == "__main__":
    main()