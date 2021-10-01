# -*- coding: utf-8 -*-

def c():
    print("Введите данные")
    a=int(input('Кол-во долек по длине\n'))
    b=int(input('Кол-во долек по ширине\n'))
    d=int(input('Кол-во долек\n'))
    print("Результат")
    if(a * b > d and (d % b == 0 or d % a == 0)):
        return "Да"
    else:
        return "Нет"
print(c())