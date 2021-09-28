n=int(input())
r=n % (60*24) // 60
p=n % 60
if (n >= 0) and (n <= 1380) and (p >= 0) and (p <= 59) and (r <= 23) and (r >= 0):
    print(r,'часы', p,'минуты')