import heapq


def heap_sort(array):
    heap = []
    for element in array:
        heapq.heappush(heap, element)  # Добавляет все элементы в кучу

    result = []
    for i in range(len(heap)):        # Извлекает каждый раз наименьший элемент из кучи
        element = heapq.heappop(heap)
        result.append(element)

    return result
