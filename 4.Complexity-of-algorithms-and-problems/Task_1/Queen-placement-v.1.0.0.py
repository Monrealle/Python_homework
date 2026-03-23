import itertools

# Переборное решение

def enumeration_solution(n):
    if n < 0:
        print("Введите неотрицательное число")
        return 0
    count = 0
    for permutation in itertools.permutations(range(n)):
        valid = True
        for i in range(n):
            for j in range(i+1, n):
                if abs(i - j) == abs(permutation[i] - permutation[j]):
                    valid = False
                    break
            if not valid:
                break
        if valid:
            count += 1
    return count

size = int(input("Введите число N: "))
result = enumeration_solution(size)
print(f"Количество решений: {result}")