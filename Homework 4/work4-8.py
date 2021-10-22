# -*- coding: utf-8 -*-

f=input('Введите строку\n')
a=f[:f.find('h')] 
b=f[f.find('h'):f.rfind('h') + 1]
c=f[f.rfind('h') + 1:]
f=a + b[::-1] + c
print(f)