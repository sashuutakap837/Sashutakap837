# -*- coding: utf-8 -*-

a=input('Введите строку\n')
if a.count('f') == 1:
    print(-1)
elif a.count('f') < 1:
    print(-2)
else:
    print(a.find('f', a.find('f') + 1))