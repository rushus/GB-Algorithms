import cProfile
import timeit

def prime(num):
    k = 1
    p = 2

    while k < num:
        p += 1

        for i in range(2, p):
            if p % i == 0:
                break
        else:
            k += 1

    return p

# print(prime(1000))
# print(timeit.timeit('prime(1000)', globals=globals(), number=1))
# 7919
# 0.31771130000000003

# cProfile.run('prime(10)')
# 4 function calls in 0.000 seconds
#
#    Ordered by: standard name
#
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.000    0.000 <string>:1(<module>)
#         1    0.000    0.000    0.000    0.000 les_4_task_2_2.py:4(prime)
#         1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

# cProfile.run('prime(100)')
# 4 function calls in 0.002 seconds
#
#    Ordered by: standard name
#
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.002    0.002 <string>:1(<module>)
#         1    0.002    0.002    0.002    0.002 les_4_task_2_2.py:4(prime)
#         1    0.000    0.000    0.002    0.002 {built-in method builtins.exec}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

# cProfile.run('prime(1000)')
# 4 function calls in 0.240 seconds
#
#    Ordered by: standard name
#
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.240    0.240 <string>:1(<module>)
#         1    0.240    0.240    0.240    0.240 les_4_task_2_2.py:4(prime)
#         1    0.000    0.000    0.240    0.240 {built-in method builtins.exec}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}