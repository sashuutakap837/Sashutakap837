# -*- coding: utf-8 -*-

a = input('Введите два слова\n')
b1 = a[:a.find(' ')]
b2 = a[a.find(' ') + 1:]
print(b2 + ' ' + b1)