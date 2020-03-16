#https://drive.google.com/file/d/1ZDjsp6i7sx-lcmwFdLcO9emWdakW_Wwn/view?usp=sharing
# Среди натуральных чисел, которые были введены, найти наибольшее по сумме цифр.
# Вывести на экран это число и сумму его цифр.

def summator(n):
    if n < 10:
        return n
    else:
        return n % 10 + summator(n // 10)


n = int(input("Введите натуральное число: "))
n_max = 0
sum_max = 0
while True:
    if n == 0:
        break
    t_num = n
    t_sum = summator(n)
    if t_sum > sum_max:
        sum_max = t_sum
        n_max = t_num
    n = int(input("Введите натуральное число: "))

if n != 0:
    print(f"Наибольшее число по сумме цифр : {n_max}, сумма равна: {sum_max}")
else:
    print("Процесс завершен")