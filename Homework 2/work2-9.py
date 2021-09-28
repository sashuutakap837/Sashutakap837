a=int(input('Введите кол-во долек по длине\n'))
b=int(input('Введите кол-во долек по ширине\n'))
c=int(input('Введите кол-во долек\n'))
s= a*b
if c <= s:
    if c == b or c == a:
        print ('Да')
    else:
        print ('Нет')
else:
    print('Нет')