# --coding: utf-8 --
a = int(input('Введите число\n'))
b = 0
while a != 0:
    f = int(input('Введите число\n'))
    if (f != 0) and (a < f):
        b += 1
    a = f
print(b)