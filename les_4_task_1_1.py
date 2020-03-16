# В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.
# 1 реализация

import random
import cProfile
import timeit

def task_1_1(size):
    min = 30
    max = 50

    array = [random.randint(min, max) for k in range(size)]
    # print("Введенный массив: ", array)

    min_id, max_id = 0, 0

    for i in range(len(array)):
        if array[i] < array[min_id]:
            min_id = i
        elif array[i] > array[max_id]:
            max_id = i

    array[min_id], array[max_id] = array[max_id], array[min_id]
    return(f"Финальный массив: {array}")

# print(timeit.timeit('task_1_1(10)', number=100, globals=globals()))
# 0.003823899999999991

# print(timeit.timeit('task_1_1(100)', number=100, globals=globals()))
# 0.032820199999999994

# print(timeit.timeit('task_1_1(1000)', number=100, globals=globals()))
# 0.1364296

# cProfile.run('task_1_1(10)')
#         66 function calls in 0.000 seconds

#   Ordered by: standard name

#   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#        1    0.000    0.000    0.000    0.000 <string>:1(<module>)
#        1    0.000    0.000    0.000    0.000 les_4_task_1_1.py:12(<listcomp>)
#        1    0.000    0.000    0.000    0.000 les_4_task_1_1.py:8(task_1_1)
#       10    0.000    0.000    0.000    0.000 random.py:174(randrange)
#       10    0.000    0.000    0.000    0.000 random.py:218(randint)
#       10    0.000    0.000    0.000    0.000 random.py:224(_randbelow)
#        1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
#        1    0.000    0.000    0.000    0.000 {built-in method builtins.len}
#       10    0.000    0.000    0.000    0.000 {method 'bit_length' of 'int' objects}
#        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#       20    0.000    0.000    0.000    0.000 {method 'getrandbits' of '_random.Random' objects}

# cProfile.run('task_1_1(100)')
#        565 function calls in 0.000 seconds
#
#    Ordered by: standard name
#
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.000    0.000 <string>:1(<module>)
#         1    0.000    0.000    0.000    0.000 les_4_task_1_1.py:12(<listcomp>)
#         1    0.000    0.000    0.000    0.000 les_4_task_1_1.py:8(task_1_1)
#       100    0.000    0.000    0.000    0.000 random.py:174(randrange)
#       100    0.000    0.000    0.000    0.000 random.py:218(randint)
#       100    0.000    0.000    0.000    0.000 random.py:224(_randbelow)
#         1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
#         1    0.000    0.000    0.000    0.000 {built-in method builtins.len}
#       100    0.000    0.000    0.000    0.000 {method 'bit_length' of 'int' objects}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#       159    0.000    0.000    0.000    0.000 {method 'getrandbits' of '_random.Random' objects}

# cProfile.run('task_1_1(1000)')
#          5490 function calls in 0.003 seconds
#
#    Ordered by: standard name
#
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.003    0.003 <string>:1(<module>)
#         1    0.000    0.000    0.002    0.002 les_4_task_1_1.py:12(<listcomp>)
#         1    0.000    0.000    0.003    0.003 les_4_task_1_1.py:8(task_1_1)
#      1000    0.001    0.000    0.002    0.000 random.py:174(randrange)
#      1000    0.000    0.000    0.002    0.000 random.py:218(randint)
#      1000    0.001    0.000    0.001    0.000 random.py:224(_randbelow)
#         1    0.000    0.000    0.003    0.003 {built-in method builtins.exec}
#         1    0.000    0.000    0.000    0.000 {built-in method builtins.len}
#      1000    0.000    0.000    0.000    0.000 {method 'bit_length' of 'int' objects}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#      1484    0.000    0.000    0.000    0.000 {method 'getrandbits' of '_random.Random' objects}