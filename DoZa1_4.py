print('Введите число')
a = int(input())
big = 0
while a > 0:
    b = a % 10
    a = a // 10
    if b > big:
        big = b

print(big)