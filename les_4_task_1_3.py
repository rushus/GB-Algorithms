# В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.
# 3 реализация

import random
import cProfile
import timeit

def task_1_3(array):

    min_id, max_id = 0, 0

    for i in range(len(array)):
        if array[i] < array[min_id]:
            min_id = i
        elif array[i] > array[max_id]:
            max_id = i

    array[min_id], array[max_id] = array[max_id], array[min_id]
    return(f"Финальный массив: {array}")

size = 1000
array = [random.randint(size * -10, size * 10) for k in range(size)]

# print(timeit.timeit('task_1_3(array)', number = 100, globals=globals())) при size = 10
# 0.000739599999999993

# print(timeit.timeit('task_1_3(array)', number=100, globals=globals())) при size = 100
# 0.002600100000000001

# print(timeit.timeit('task_1_3(array)', number=100, globals=globals())) при size = 1000
# 0.020445000000000005

# cProfile.run('task_1_3(array)')
#         5 function calls in 0.000 seconds
#
#    Ordered by: standard name
#
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.000    0.000 <string>:1(<module>)
#         1    0.000    0.000    0.000    0.000 les_4_task_1_3.py:8(task_1_3)
#         1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
#         1    0.000    0.000    0.000    0.000 {built-in method builtins.len}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

# Вывод: Третий вариант оказался по времени лучше двух других. Причиной, вероятно, послужило то, что
# в третьем варианте мы вынесли создание массива за пределы функции - за работу программы оно выполняется единожды.