def n_queens_easy(n):
    if n <= 0:
        print("Введите неотрицательное число")
        return 0
    count = 0
    array = [0] * n
    
    def check(line, column):
        for i in range(line):
            if array[i] == column or abs(array[i] - column) == abs(i - line):
                return False
        return True
    
    def solve(line):
        nonlocal count
        if line == n:
            count += 1
            return
        
        for column in range(n):
            if check(line, column):
                array[line] = column
                solve(line + 1)
    
    solve(0)
    return count

size = int(input("Введите число N: "))
result = n_queens_easy(size)
print(f"Количество решений: {result}")
