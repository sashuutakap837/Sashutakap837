# -*- coding: utf-8 -*-

a = int(input('Введите число\n'))
b = int(input('Введите число\n'))
for i in range(a - (a + 1) % 2, b - b % 2, -2):
    print(i, end=' ')