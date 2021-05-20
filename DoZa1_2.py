print('Введите время в секундах')
time = int(input())

sek = time % 60

time = time // 60

mins = time % 60

time = time // 60

print(time, mins, sek)
