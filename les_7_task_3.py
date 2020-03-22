# Массив размером 2m + 1, где m — натуральное число, заполнен случайным образом. Найдите в массиве медиану.
# Медианой называется элемент ряда, делящий его на две равные части: в одной находятся элементы, которые
# не меньше медианы, в другой — не больше медианы.

import random

def gnome_sort(array):
    i = 0

    while i < len(array):
        if i == 0:
            i = i + 1
        if array[i] >= array[i - 1]:
            i = i + 1
        else:
            array[i], array[i - 1] = array[i - 1], array[i]
            i = i - 1

    return array


m = int(input("Введите параметр m: "))
array = [random.randint(0, 50) for i in range(2*m + 1)]
print("Исходный массив:\n", array)
print("\nОтсортированный массив:\n", gnome_sort(array))
print("\nМедиана: ", array[len(array) // 2])
