# Написать программу сложения и умножения двух шестнадцатеричных чисел. При этом каждое число представляется
# как коллекция, элементы которой — цифры числа. Например, пользователь ввёл A2 и C4F. Нужно сохранить их
# как [‘A’, ‘2’] и [‘C’, ‘4’, ‘F’] соответственно. Сумма чисел из примера: [‘C’, ‘F’, ‘1’],
# произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].

from collections import deque

BtH = ('0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F')

HtB = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, 'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15}

def summ(a, b):
    a = a.copy()
    b = b.copy()

    if len(a) < len(b):
        a, b = b, a

    b.extendleft('0' * (len(a) - len(b)))

    t = 0
    res = deque()
    for i in range(len(a)):
        a_num = HtB[a.pop()]
        b_num = HtB[b.pop()]

        res_num = a_num + b_num + t

        if res_num >= 16:
            t = 1
            res_num -= 16
        else:
            t = 0

        res.appendleft(BtH[res_num])

        i += 1

    if t != 0:
        res.appendleft(f'{t}')

    return res

def multi(a, b):
    a = a.copy()
    b = b.copy()

    if len(a) < len(b):
        a, b = b, a

    b.extendleft('0' * (len(a) - len(b)))

    res = deque('0')
    for i in range(len(b)):
        b_num = HtB[b.pop()]

        t = deque('0')
        for k in range(b_num):
            t = summ(t, a)

        t.extend('0' * (len(a) - len(b) - 1))
        res = summ(res, t)

        i += 1

    return res


x = deque(input('Введите 1 число в 16-ричной системе: ').upper())
y = deque(input('Введите 2 число в 16-ричной системе: ').upper())

print(f'{list(x)} + {list(y)} = {list(summ(x, y))}')
print(f'{list(x)} * {list(y)} = {list(multi(x, y))}')