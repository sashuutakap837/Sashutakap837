# -*- coding: utf-8 -*-

def c():
    print("Введите данные")
    a=int(input("Расстояние между рядами\n"))
    n=int(input("Расстояние между дырочками\n"))
    i=int(input("Длина свободного конца шнурка\n"))
    N=int(input("Кол-во дырочек в ряду\n"))
    print("Длина шнурков\n")
    return (2 * N - 1) * a + 2 * i + 2 * (N - 1) * n 
print(c())