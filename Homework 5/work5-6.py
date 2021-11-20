# --coding: utf-8 --
a = 0
b = 0
c = int(input('Введите число\n'))
while c != 0:
    a = a + c
    b = b + 1
    c = int(input('Введите число\n'))
print(a / b)