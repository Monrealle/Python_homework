class Matrix:
    def __init__(self, data):
        self._data = data
        self.rows = len(data)
        self.cols = len(data[0])

    # Сложение матриц
    def __add__(self, other):
        result = [
            [self._data[i][j] + other._data[i][j] for j in range(self.cols)]
            for i in range(self.rows)
        ]
        return Matrix(result)

    # Умножение на константу
    def __mul__(self, scalar):
        result = [
            [self._data[i][j] * scalar for j in range(self.cols)]
            for i in range(self.rows)
        ]
        return Matrix(result)

    # Умножение матриц
    def __matmul__(self, other):
        result = [[0] * other.cols for _ in range(self.rows)]
        for i in range(self.rows):
            for j in range(other.cols):
                for k in range(self.cols):
                    result[i][j] += self._data[i][k] * other._data[k][j]
        return Matrix(result)

    # Итерирование по матрице
    def __iter__(self):
        for row in self._data:
            for element in row:
                yield element

    # Вычисление определителя
    def determinant(self):
        return self._det(self._data)

    def _det(self, matrix):
        n = len(matrix)
        if n == 1:
            return matrix[0][0]
        if n == 2:
            return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]

        det = 0
        for col in range(n):
            minor = [
                [matrix[i][j] for j in range(n) if j != col]
                for i in range(1, n)
            ]
            det += ((-1) ** col) * matrix[0][col] * self._det(minor)
        return det
