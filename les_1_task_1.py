#https://drive.google.com/file/d/1R0ArzrxutAxOkNHihKv83Mx81i7jrFsi/view?usp=sharing
#Найти сумму и произведение цифр трехзначного числа, которое вводит пользователь.

s = int(input("Введите трехзначное число: "))

summat = 0
multi = 1


summat += s % 10
multi *= s % 10
s //= 10

summat += s % 10
multi *= s % 10
s //= 10

summat += s % 10
multi *= s % 10
s //= 10

print("Сумма: {}\nПроизведение: {}".format(summat, multi))