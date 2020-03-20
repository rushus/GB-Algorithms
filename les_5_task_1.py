# Пользователь вводит данные о количестве предприятий, их наименования и прибыль за 4 квартал (т.е. 4 числа)
# для каждого предприятия. Программа должна определить среднюю прибыль (за год для всех предприятий) и отдельно вывести
# наименования предприятий, чья прибыль выше среднего и ниже среднего.
from collections import namedtuple

Company = namedtuple('Company', 'name income')
companies = set()
all_income = 0

n = int(input("Всего предприятий: "))

for i in range(n):
    name = input(f"\n{i+1}-е предприятие: ")
    income = 0

    quarters = []
    for j in range(4):
        quarters.append(int(input(f"Прибыль за {j+1}-й квартал: ")))
        income += quarters[j]

    cmp = Company(name = name, income = income)

    companies.add(cmp)
    all_income += income

avrg = all_income / n
print("\nСредняя прибыль: ", avrg)

print("\nПрибыль выше среднего:")
for c in companies:
    if c.income > avrg:
        print(f"Прибыль компании {c.name} составила {c.income}")

print("\nПрибыль ниже среднего:")
for c in companies:
    if c.income < avrg:
        print(f'Прибыль компании {c.name} составила {c.income}')