import pytest
from heap_sort import heap_sort


def test_unit_tests(): # unit тесты
    
    assert heap_sort([3, 1, 2]) == [1, 2, 3]

    assert heap_sort([2, 7, 15, 23, 4, 9, 22]) == [2, 4, 7, 9, 15, 22, 23]

    assert heap_sort([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]

    assert heap_sort([5, 4, 3, 2, 1]) == [1, 2, 3, 4, 5]


def test_extreme_cases(): # Крайние случаи

    assert heap_sort([]) == []

    assert heap_sort([-3, -2, -1]) == [-3, -2, -1]

    assert heap_sort([-1, -2, -3]) == [-3, -2, -1]

    assert heap_sort([0, 1, 7, -5, -2,]) == [-5, -2, 0, 1, 7]


def test_property_based_tests(): # Property based тесты с другими сортировками

    def quik_sort(array):
        if len(array) <= 1:
            return array
        
        else:
            pivot = array[len(array) // 2]
            left = [x for x in array if x < pivot]
            right = [x for x in array if x > pivot]
            middle = [x for x in array if x == pivot]

            return quik_sort(left) + middle + quik_sort(right)
        

    def bubble_sort(array):
        array = array.copy()

        for i in range(len(array)):
            for j in range(0, len(array) - i - 1):
                if array[j] > array[j + 1]:
                    array[j], array[j + 1] = array[j + 1], array[j]

        return array


    @pytest.mark.parametrize(
        ["input_arr", "expected"],
        [   ([3, 1, 2], [1, 2, 3]),
            ([2, 7, 15, 23, 4, 9, 22], [2, 4, 7, 9, 15, 22, 23]),
            ([1, 2, 3, 4, 5], [1, 2, 3, 4, 5]),
            ([5, 4, 3, 2, 1], [1, 2, 3, 4, 5]),
            ([], []),
            ([-3, -2, -1], [-3, -2, -1]),
            ([-1, -3, -2], [-3, -2, -1]),
            ([-1, -2, -3], [-3, -2, -1]),
            ([0, 1, 7, -5, -2,], [-5, -2, 0, 1, 7]),
        ]
    )
    def test_with_other_sortings(input_arr):
        assert heap_sort(input_arr) == quik_sort(input_arr)

        assert heap_sort(input_arr) == bubble_sort(input_arr)

        assert heap_sort(input_arr) == sorted(input_arr)
