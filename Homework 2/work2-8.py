a=int(input('Введите 1ое число\n'))
b=int(input('Введите 2ое число\n'))
c=int(input('Введите 3е число\n'))
if a == b or a == c or c == b:
    print ('Есть совпадения','',2)
elif a == b == c:
    print ('Есть совпадения','',3)
else:
    print('Совпадений нет','',0)
    