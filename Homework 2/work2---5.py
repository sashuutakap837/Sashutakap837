# -*- coding: utf-8 -*-

def c():
    print("Ведите данные")
    a=int(input())
    b=int(input())
    d=int(input())
    print("Наименьшее число")
    return min(a,b,d)
print(c())