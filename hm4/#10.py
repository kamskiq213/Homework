n = int(input('Введите число n: '))
for i in range(2,n+1,2):
    if n % i ==0:
        print(i)