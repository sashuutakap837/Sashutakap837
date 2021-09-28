# -- coding: utf-8 --
x = 18
name = 'Александр'
age = 10
if (age > 0) and (age >= 16) and (age < 75) and (name != 'Иван'):
    print('Поздравляю вы поступили в ВГУИТ!')
elif age < 16: print('Сначала нужно окончить школу! Вам осталось',x-age,'лет.')