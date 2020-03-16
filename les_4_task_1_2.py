# В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.
# 2 реализация

import random
import cProfile
import timeit

#size = int(input("Пожалуйста, введите размер массива: "))
#min = int(input("Пожалуйста, введите минимальный элемент: "))
#max = int(input("Пожалуйста, введите максимальный элемент: "))
def task_1_2(size):
    array = [random.randint(size * -10, size * 10) for k in range(size)]
    #print("Введенный массив: ", array)

    min_id, max_id = 0, 0

    for i in range(len(array)):
        if array[i] < array[min_id]:
            min_id = i
        elif array[i] > array[max_id]:
            max_id = i

    array[min_id], array[max_id] = array[max_id], array[min_id]
    return f"Финальный массив: {array}"


# print(timeit.timeit('task_1_2(10)', number=100, globals=globals()))
# 0.003458700000000009

# print(timeit.timeit('task_1_2(100)', number=100, globals=globals()))
# 0.015593999999999997

# print(timeit.timeit('task_1_2(1000)', number=100, globals=globals()))
# 0.1641241

#cProfile.run('task_1_2(10)')
#         61 function calls in 0.000 seconds
#   Ordered by: standard name

#   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#        1    0.000    0.000    0.000    0.000 <string>:1(<module>)
#        1    0.000    0.000    0.000    0.000 les_4_task_1_2.py:10(task_1)
#        1    0.000    0.000    0.000    0.000 les_4_task_1_2.py:11(<listcomp>)
#       10    0.000    0.000    0.000    0.000 random.py:174(randrange)
#       10    0.000    0.000    0.000    0.000 random.py:218(randint)
#       10    0.000    0.000    0.000    0.000 random.py:224(_randbelow)
#        1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
#        1    0.000    0.000    0.000    0.000 {built-in method builtins.len}
#       10    0.000    0.000    0.000    0.000 {method 'bit_length' of 'int' objects}
#        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#       15    0.000    0.000    0.000    0.000 {method 'getrandbits' of '_random.Random' objects}

#cProfile.run('task_1_2(100)')
#        508 function calls in 0.001 seconds

#   Ordered by: standard name

#   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#        1    0.000    0.000    0.001    0.001 <string>:1(<module>)
#        1    0.000    0.000    0.001    0.001 les_4_task_1_2.py:10(task_1)
#        1    0.000    0.000    0.001    0.001 les_4_task_1_2.py:11(<listcomp>)
#      100    0.000    0.000    0.001    0.000 random.py:174(randrange)
#      100    0.000    0.000    0.001    0.000 random.py:218(randint)
#      100    0.000    0.000    0.000    0.000 random.py:224(_randbelow)
#        1    0.000    0.000    0.001    0.001 {built-in method builtins.exec}
#        1    0.000    0.000    0.000    0.000 {built-in method builtins.len}
#      100    0.000    0.000    0.000    0.000 {method 'bit_length' of 'int' objects}
#        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#      102    0.000    0.000    0.000    0.000 {method 'getrandbits' of '_random.Random' objects}

#cProfile.run('task_1_2(1000)')
#          5675 function calls in 0.010 seconds
#
#    Ordered by: standard name
#
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.010    0.010 <string>:1(<module>)
#         1    0.001    0.001    0.010    0.010 les_4_task_1_2.py:10(task_1)
#         1    0.001    0.001    0.009    0.009 les_4_task_1_2.py:11(<listcomp>)
#      1000    0.003    0.000    0.006    0.000 random.py:174(randrange)
#      1000    0.001    0.000    0.007    0.000 random.py:218(randint)
#      1000    0.002    0.000    0.003    0.000 random.py:224(_randbelow)
#         1    0.000    0.000    0.010    0.010 {built-in method builtins.exec}
#         1    0.000    0.000    0.000    0.000 {built-in method builtins.len}
#      1000    0.000    0.000    0.000    0.000 {method 'bit_length' of 'int' objects}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#      1669    0.001    0.000    0.001    0.000 {method 'getrandbits' of '_random.Random' objects}