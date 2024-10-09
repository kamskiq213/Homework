from random import randint

n = []

for i in range(10):
    n.append(randint(1, 900))
for num in n:
    print(num) # 3

print(n.clear()) # 4