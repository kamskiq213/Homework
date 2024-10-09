from random import randint

a = int(input('Укажите длину списка: '))

n = []

for i in range(a):
    b = randint(1, 9999)
    n.append(b)

max1 = max(n)
n.remove(max1)
max2 = max(n)
print(f'Второй максимум: {max2}')