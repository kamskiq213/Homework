from random import randint

a = int(input('Укажите длину списка: '))

n = []
sum= 0
avg = 0
for i in range(a):
    b = randint(1, 9999)
    n.append(b)
    sum+=b

print(f'Наибольший элемент списка: {max(n)}')
print(f'Наибольший элемент списка: {min(n)}')
print(f'Сумма элементов списка: {sum}')
print(f'Среднее арифметическое списка: {sum/a}')