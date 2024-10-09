from random import randint

a = int(input('Укажите длину списка: '))

n = []
local=[]
for i in range(a):
    b = randint(1, 9999)
    n.append(b)

for i in range(1,len(n)-1):
    if n[i] > n[i-1] and n[i] > n[i+1]:
        local.append(n[i])
print(f'Последний локальный максимум: {local[-1]}')
