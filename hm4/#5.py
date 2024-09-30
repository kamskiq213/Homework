n = int(input("Введите кол-во чисел: "))

sum=0
proiz=1
avg=0

for i in range(n):
    num = int(input("Введите число: "))
    sum+=num
    proiz*=num
    avg+=num
print(f'Сумма чисел: {sum}')
print(f'Произведение чисел: {proiz}')
print(f'Среднее арифметическое чисел: {avg/n}')