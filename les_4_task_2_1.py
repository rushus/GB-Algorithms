import cProfile
import timeit
import math

def SieveOfEratosthenes(n):
    MULTIPLIER = 1.3
    size = int(n * math.log(n) * MULTIPLIER) if n > 10 else 30
    prime = [True for _ in range(size + 1)]
    prime[0] = False
    prime[1] = False
    p = 2
    k = 0
    #*p
    while (p  <= size):
        if (prime[p] == True):

            k += 1
            if k == n:
                return p

            for i in range(p * 2, size + 1, p):
                prime[i] = False
        p += 1

#print(SieveOfEratosthenes(1000))
#print(timeit.timeit('SieveOfEratosthenes(1000)', globals=globals(), number=1))
# 7919
# 0.0061692

# cProfile.run('SieveOfEratosthenes(10)')
# 2 function calls in 0.000 seconds
#
#    Ordered by: standard name
#
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

# cProfile.run('SieveOfEratosthenes(100)')
# 6 function calls in 0.000 seconds
#
#    Ordered by: standard name
#
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.000    0.000 <string>:1(<module>)
#         1    0.000    0.000    0.000    0.000 les_4_task_2_1.py:5(SieveOfEratosthenes)
#         1    0.000    0.000    0.000    0.000 les_4_task_2_1.py:8(<listcomp>)
#         1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
#         1    0.000    0.000    0.000    0.000 {built-in method math.log}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

# cProfile.run('SieveOfEratosthenes(1000)')
# 6 function calls in 0.014 seconds
#
#    Ordered by: standard name
#
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.013    0.013 <string>:1(<module>)
#         1    0.012    0.012    0.013    0.013 les_4_task_2_1.py:5(SieveOfEratosthenes)
#         1    0.001    0.001    0.001    0.001 les_4_task_2_1.py:8(<listcomp>)
#         1    0.000    0.000    0.014    0.014 {built-in method builtins.exec}
#         1    0.000    0.000    0.000    0.000 {built-in method math.log}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
