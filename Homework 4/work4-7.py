# -*- coding: utf-8 -*-

a=input('Введите строку\n')
b = a.find('h') 
c = a.rfind('h')    
print(a[:b] + a[c + ( c != -1):])