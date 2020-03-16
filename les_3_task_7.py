# В одномерном массиве целых чисел определить два наименьших элемента. Они могут быть как равны между собой
# (оба являться минимальными), так и различаться.

import random

size = int(input("Пожалуйста, введите размер массива: "))
min = int(input("Пожалуйста, введите минимальный элемент: "))
max = int(input("Пожалуйста, введите максимальный элемент: "))

array = [random.randint(min, max) for k in range(size)]
print("Введенный массив: ", array)

if array[0] < array[1]:
    min_1 = 0
    min_2 = 1
else:
    min_1 = 1
    min_2 = 0


for i in range(2, len(array)):
    if array[i] < array[min_1]:
        temp = min_1
        min_1 = i
        if array[temp] < array[min_2]:
            min_2 = temp
    elif array[i] < array[min_2]:
        min_2 = i

print(f"Первый наименьший элемент: {array[min_1]}. Второй наименьший элемент: {array[min_2]}")
