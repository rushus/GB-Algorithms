#https://drive.google.com/file/d/1ZDjsp6i7sx-lcmwFdLcO9emWdakW_Wwn/view?usp=sharing
#Напишите программу, доказывающую или проверяющую, что для множества натуральных чисел выполняется равенство:
# 1+2+...+n = n(n+1)/2, где n - любое натуральное число

def funSum(n):
    summ = 0
    while n != 0:
        summ += n
        n -= 1
    return summ

def funOper(n):
    return n*(n+1)/2

n = int(input("Введите натуральное число n: "))


first = funSum(n)
second = funOper(n)

if first == second:
    print(f"Равенство выполняется: {first} = {second}")
else:
    print("Равенство не выполнено")
