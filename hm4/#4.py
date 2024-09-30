n = int(input('Введите кол-во дней: '))
day1 = int(input('Введите курс на первый день: '))
proc = int(input('Введите процент изменения: '))

for i in range(1,n+1):
    day1 = day1 + day1 * (proc / 100)
    print(day1)