# -*- coding: utf-8 -*-

def c():
    print("Введите данные")
    a=int(input("Номер года\n"))
    print("Результат")
    if((a % 4 == 0 and a % 100 != 0) or a % 400 == 0):
        return "Да"
    else:
        return "Нет"
print(c())    