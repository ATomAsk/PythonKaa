#Реализовать функцию, принимающую несколько параметров,
# описывающих данные пользователя: имя, фамилия, год рождения, город проживания, email, телефон.
# Функция должна принимать параметры как именованные аргументы.
# Реализовать вывод данных о пользователе одной строкой.

def my_func(name, surn, date, adr, mail, phnmb):
    print(f"Имя - {name}; фамилия - {surn}; дата рождения - {date}; адрес - {adr}; эл.почта - {mail}; номер телефона - {phnmb}")

a = 'да'

while (a == 'да') or (a == 'Да') :
    gname = str(input('Введите имя : '))
    gsurn = str(input('Введите фамилию: '))
    gdate = str(input('Введите дату рождения: '))
    gadr = str(input('Введите город проживания: '))
    gmail = str(input('Введите email: '))
    gphnmb = str(input('Введите номер телефона: '))

    my_func(name = gname, surn = gsurn, date = gdate, adr = gadr, mail = gmail, phnmb = gphnmb)

    a = str(input('Продолжаем? ' ))
print('До свиданья')



