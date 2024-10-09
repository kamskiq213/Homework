from random import randint

a = int(input('Укажите длину списка: '))

n = []
m=[]
for i in range(a):
    b = randint(1, 9999)
    n.append(b)

for i in n:
    if i not in m: 
        m.append(i)
print(f'Количество разных элементов списка: {len(m)}')