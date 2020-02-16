#https://drive.google.com/file/d/1R0ArzrxutAxOkNHihKv83Mx81i7jrFsi/view?usp=sharing
# Вводятся три разных числа. Найти, какое из них является средним (больше одного, но меньше другого)
print("Введите три разных числа")
a = float(input("Введите первое число: "))
b = float(input("Введите второе число: "))
c = float(input("Введите третье число: "))


if (a < b and a > c) or (a > b and a < c):
    print(a)
elif (b < a and b > c) or (b > a and b < c):
    print(b)
else:
    print(c)