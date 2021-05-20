print('Введите прибыль фирмы')
profit = int(input())

print('Введите издержки фирмы')
costs = int(input())

if (profit - costs) < 0:
    print('Фирма в убытке')
else:
    print('Фирма получает прибыль. Рентабельность составляет', (profit - costs))

print('Введите численность персонала фирмы')
qntt = int(input())
print('Прибыль фирмы на одного сотрудника составляет', (profit / qntt))

