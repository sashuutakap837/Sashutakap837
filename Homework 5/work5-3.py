# --coding: utf-8 --
a = int(input('Введите число\n'))
b = 1
c = 0
while b <= a:
    b = b*2
    c = c+1
    if b <= a:
        print(b, c)