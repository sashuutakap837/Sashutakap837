# -*- coding: utf-8 -*-

n = int(input('Введите кол-во ступенек\n'))
for i in range(1, n + 1):
    for a in range(1, i + 1):
        print(a, sep='', end='')
    print()