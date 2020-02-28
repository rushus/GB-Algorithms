#https://drive.google.com/file/d/1ZDjsp6i7sx-lcmwFdLcO9emWdakW_Wwn/view?usp=sharing
# Найти сумму n элементов следующего ряда чисел: 1, -0.5, 0.25, -0.125,… Количество элементов (n) вводится с клавиатуры.

n = int(input("Введите n: "))
i = 1
num = 1
sum = 0
while i <= n:
    sum += num
    num /= -2
    i += 1

print(sum)
