class FrozenMatrix:
    def __init__(self, matrix):
        if isinstance(matrix, (list, tuple)):
            self._matrix = tuple(tuple(row) for row in matrix)
        elif isinstance(matrix, FrozenMatrix):
            self._matrix = matrix._matrix
        else:
            raise TypeError("Ошибка")

    @property
    def shape(self):
        if not self._matrix:
            return (0, 0)
        return (len(self._matrix), len(self._matrix[0]))

    def __hash__(self):
        return hash(self._matrix)

    def __eq__(self, other):
        if not isinstance(other, FrozenMatrix):
            return False
        return self._matrix == other._matrix

    def __getitem__(self, key):
        if isinstance(key, tuple):
            row, col = key
            return self._matrix[row][col]
        return self._matrix[key]

    def __iter__(self):
        return iter(self._matrix)

    def __repr__(self):
        return f"FrozenMatrix({list(list(row) for row in self._matrix)})"

    def __str__(self):
        rows = ["[" + ", ".join(map(str, row)) + "]" for row in self._matrix]
        return "[" + ",\n ".join(rows) + "]"

    def __len__(self):
        return len(self._matrix)
