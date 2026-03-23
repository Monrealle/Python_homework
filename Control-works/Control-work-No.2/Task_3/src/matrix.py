import numpy as np

def save_mtx(matrix, filename):
    """Сохраняет матрицу в MTX формате"""
    rows, cols = matrix.shape

    with open(filename, 'w') as f:
        f.write("%%MatrixMarket matrix coordinate real general\n")

        # Считаем ненулевые элементы
        nonzero = []
        for i in range(rows):
            for j in range(cols):
                if matrix[i, j] != 0:
                    nonzero.append((i+1, j+1, matrix[i, j]))

        # Размеры
        f.write(f"{rows} {cols} {len(nonzero)}\n")

        # Данные
        for i, j, val in nonzero:
            f.write(f"{i} {j} {val:.15g}\n")

def load_mtx(filename):
    """Загружает матрицу из MTX формата"""
    with open(filename, 'r') as f:
        lines = f.readlines()

    data_lines = []
    for line in lines:
        line = line.strip()
        if line and not line.startswith('%'):
            data_lines.append(line)

    if not data_lines:
        raise ValueError("Файл не содержит данных")

    rows, cols, nnz = map(int, data_lines[0].split())

    # Создаем матрицу
    matrix = np.zeros((rows, cols))

    for i in range(1, len(data_lines)):
        parts = data_lines[i].split()
        if len(parts) >= 3:
            r, c = int(parts[0])-1, int(parts[1])-1
            val = float(parts[2])
            matrix[r, c] = val

    return matrix

if __name__ == "__main__":
    mat = np.array([
        [1, 0, 3],
        [0, 5, 0],
        [7, 0, 9]
    ])

    # Сохраняем
    save_mtx(mat, "simple.mtx")

    # Загружаем
    loaded = load_mtx("simple.mtx")

    print("Исходная матрица:")
    print(mat)
    print("\nЗагруженная матрица:")
    print(loaded)

    print("\nСовпадают?", np.allclose(mat, loaded))
