# В одномерном массиве найти сумму элементов, находящихся между минимальным и максимальным элементами.
# Сами минимальный и максимальный элементы в сумму не включать.

import random

size = int(input("Пожалуйста, введите размер массива: "))
min = int(input("Пожалуйста, введите минимальный элемент: "))
max = int(input("Пожалуйста, введите максимальный элемент: "))

array = [random.randint(min, max) for k in range(size)]
print("Введенный массив: ", array)

min_id, max_id = 0, 0

for i in range(1, len(array)):
    if array[i] < array[min_id]:
        min_id = i
    elif array[i] > array[max_id]:
       max_id = i

if min_id > max_id:
    min_id, max_id = max_id, min_id

print(f"Отрезок суммирования: от {array[min_id]} до {array[max_id]}")

s = 0
for i in range(min_id + 1, max_id):
    s = s + array[i]
print(f'Сумма равна: {s}')