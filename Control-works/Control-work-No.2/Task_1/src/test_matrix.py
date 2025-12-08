from matrix_package import Matrix

def test_matrix():
    """Тест matrix.py"""
    print("\nТЕСТ MATRIX.PY:")

    # 1. Создание матрицы
    M = Matrix([[1, 2], [3, 4]])
    print(f"1. Матрица: {M._data}")

    # 2. Сложение
    M2 = M + M
    print(f"2. M + M: {M2._data}")

    # 3. Умножение на константу
    M3 = M * 5
    print(f"3. M * 5: {M3._data}")

    # 4. Умножение матриц
    A = Matrix([[1, 2], [3, 4]])
    B = Matrix([[2, 0], [1, 2]])
    C = A @ B
    print(f"4. A @ B: {C._data}")

    # 5. Определитель
    det = M.determinant()
    print(f"5. det(M): {det}")

    # 6. Итерация
    print(f"6. Элементы M:", end=" ")
    for elem in M:
        print(elem, end=" ")
    print()

if __name__ == "__main__":
    # Запуск тестов
    test_matrix()
