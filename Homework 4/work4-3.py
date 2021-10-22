# -*- coding: utf-8 -*-

a = input('Введите строку символов\n')
print(a[(len(a) + 1) // 2:] + a[:(len(a) + 1) // 2])