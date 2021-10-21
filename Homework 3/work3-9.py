# -*- coding: utf-8 -*-

n = int(input('Введите кол-во чисел:'))
f1 = 0
f2 = 1
b = 0
sum = 1
if n >= 3:
    for i in range(n - 2):
        b = f1 + f2
        sum = sum + b
        f1 = f2
        f2 = b
    print(sum)