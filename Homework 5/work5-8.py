# --coding: utf-8 --
a = -1
b = 0
c = 0
f = int(input('Введите число\n'))
while f != 0:
    if a == f:
        b = b+1
    else:
        a = f
        c = max(c, b)
        b = 1
    f = int(input('Введите число\n'))
c = max (c, b)
print(c)