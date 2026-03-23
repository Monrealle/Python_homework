from multiprocessing import Pool
from multiprocessing import cpu_count


# Быстрое решение
def recursive_solution(n):
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


def wrapper(args):
    n, first_col = args

    array = [first_col] + [0] * (n - 1)
    count = 0

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

    solve(1)
    return count


def parallel_solution(n):
    if n <= 0:
        print("Введите неотрицательное число")
        return 0

    tasks = [(n, col) for col in range(n)]

    with Pool(processes=cpu_count()) as pool:
        results = pool.map(wrapper, tasks)

    return sum(results)


if __name__ == "__main__":
    size = int(input("Введите число N: "))

    if size <= 8:
        result = recursive_solution(size)
    else:
        result = parallel_solution(size)

    print(f"Количество решений: {result}")
