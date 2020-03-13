# В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.

import random

size = int(input("Пожалуйста, введите размер массива: "))
min = int(input("Пожалуйста, введите минимальный элемент: "))
max = int(input("Пожалуйста, введите максимальный элемент: "))

array = [random.randint(min, max) for k in range(size)]
print("Введенный массив: ", array)

min_id, max_id = 0, 0

for i in range(len(array)):
    if array[i] < array[min_id]:
        min_id = i
    elif array[i] > array[max_id]:
        max_id = i

array[min_id], array[max_id] = array[max_id], array[min_id]
print(f"Финальный массив: {array}")
