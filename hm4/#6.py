n = int(input("Введите количество лет: "))
p = int(input("Введите начальную численность населения: "))
r = int(input("Введите процентный прирост: "))

for i in range(1, n+1):
    p = p + (p*(r/100))

print(f'Население через {n} лет: {int(p)} ')