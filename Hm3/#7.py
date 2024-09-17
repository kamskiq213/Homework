n = int(input('Введите n: '))
x = int(input('Введите x: '))

sum=0

for i in range(1, n+1):
    sum+=1/(x**(2*i-2))
print(sum)
        
            