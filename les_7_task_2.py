# Отсортируйте по возрастанию методом слияния одномерный вещественный массив, заданный случайными
# числами на промежутке [0; 50). Выведите на экран исходный и отсортированный массивы.

import random

def merge_sort(array):
    if len(array) > 1:

        L = merge_sort(array[: len(array) // 2])
        R = merge_sort(array[len(array) // 2 :])

        i = 0
        j = 0
        k = 0

        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                array[k] = L[i]
                i += 1
            else:
                array[k] = R[j]
                j += 1
            k += 1

        while i < len(L):
            array[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            array[k] = R[j]
            j += 1
            k += 1
    return array


array = [round(random.uniform(0, 50), 3) for i in range(10)]
print("Исходный массив:\n", array)
print("\nОтсортированный массив:\n", merge_sort(array))
