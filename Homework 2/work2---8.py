# -*- coding: utf-8 -*-

def c():
    print("Введите данные")
    a=int(input('Введите 1ое число\n'))
    b=int(input('Введите 2ое число\n'))
    d=int(input('Введите 3е число\n'))
    print ("Совпадений")
    if (a == b == d):
        return 3
    elif (a == b or a == d or d == c):
        return 2
    else:
        return 0
print (c())