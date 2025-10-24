def curry(func, arity):
    """
    Преобразует обычную функцию в каррированную функцию

    Args:
        func: исходная функция
        arity: количество аргументов, которые должна принять функция
    """
    if arity < 0:
        raise ValueError("Арность не может быть отрицательной")

    def curried(*args):
        if len(args) > arity:
            raise TypeError("Передано больше аргументов, чем ожидается")

        if len(args) == arity:
            return func(*args)

        else:
            return lambda x: curried(*(args + (x,)))

    return curried


def uncurry(curried_func, arity):
    """
    Преобразует каррированную функцию в обычную

    Args:
        curried_func: каррированная функция
        arity: арность исходной функции
    """
    if arity < 0:
        raise ValueError("Арность не может быть отрицательной")

    def uncurried(*args):
        if len(args) != arity:
            raise TypeError("Функция ожидает другое количество аргументов")

        result = curried_func

        for arg in args:
            result = result(arg)

        return result

    return uncurried


def sum(x, y, z):
    return x + y + z


# Тестирование
if __name__ == "__main__":
    sum_curry = curry(sum, 3)
    sum_uncurry = uncurry(sum_curry, 3)

    print(sum_curry(1)(2)(3))  # 6
    print(sum_uncurry(1, 2, 3))  # 6

    try:
        sum_curry(1)(2)(3)(4)  # Слишком много аргументов
    except TypeError as e:
        print(f"Ошибка: {e}")

    try:
        curry(sum, -1)  # Отрицательная арность
    except ValueError as e:
        print(f"Ошибка: {e}")
