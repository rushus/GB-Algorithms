# Подсчитать, сколько было выделено памяти под переменные в ранее разработанных программах в рамках первых трех уроков.
# Проанализировать результат и определить программы с наиболее эффективным использованием памяти.
# реализация 3

import sys


def task_1_3(array):

    min_id, max_id = 0, 0

    for i in range(len(array)):
        if array[i] < array[min_id]:
            min_id = i
        elif array[i] > array[max_id]:
            max_id = i

    array[min_id], array[max_id] = array[max_id], array[min_id]
    all_memory([min_id, max_id, array])
    return(f"Финальный массив: {array}")

size = 1000
#array = [random.randint(size * -10, size * 10) for k in range(size)] #заменил рандомный array на статичный
array = [50, 46, 38, 35, 31, 39, 42, 38, 42, 50]                      #для точного сравнения памяти


def memory_size(obj):
    global result

    print(f'type={type(obj)}, size={sys.getsizeof(obj)}, obj={obj}')
    if hasattr(obj, '__iter__'):
        if hasattr(obj, 'items'):
            for key, value in obj.items():
                memory_size(key)
                memory_size(value)
        elif not isinstance(obj, str):
            for item in obj:
                memory_size(item)
    result += sys.getsizeof(obj)

def all_memory(obj):
    global result

    memory_size(obj)
    result -= sys.getsizeof(obj)
    print("Общий объем выделенной памяти под переменные равен ", result)


result = 0
task_1_3(array)

#Python 3.7.2 (tags/v3.7.2:9a3ffc0492, Dec 23 2018, 23:09:28) [MSC v.1916 64 bit (AMD64)] on win32
# type=<class 'list'>, size=88, obj=[4, 0, [31, 46, 38, 35, 50, 39, 42, 38, 42, 50]]
# type=<class 'int'>, size=28, obj=4
# type=<class 'int'>, size=24, obj=0
# type=<class 'list'>, size=144, obj=[31, 46, 38, 35, 50, 39, 42, 38, 42, 50]
# type=<class 'int'>, size=28, obj=31
# type=<class 'int'>, size=28, obj=46
# type=<class 'int'>, size=28, obj=38
# type=<class 'int'>, size=28, obj=35
# type=<class 'int'>, size=28, obj=50
# type=<class 'int'>, size=28, obj=39
# type=<class 'int'>, size=28, obj=42
# type=<class 'int'>, size=28, obj=38
# type=<class 'int'>, size=28, obj=42
# type=<class 'int'>, size=28, obj=50
# Общий объем выделенной памяти под переменные равен  476

# Вывод: реализации 2 и 3 оказались лучше в плане эффективности использования памяти, так как у них отсутствуют
#        переменные min и max, использовавшиеся в методе random.