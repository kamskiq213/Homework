k = int(input('Введите число 1: '))
n = int(input('Введите число 2: '))

sum= 0 

for i in range(k, n+1):
    if i % 2 == 0:
        sum += i
print(sum)