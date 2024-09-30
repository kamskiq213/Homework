n = int(input("Введите число n : "))

for i in range(1, n+1):
    if i < 100:
        if i % 10 == i // 10:
            print(i)
    elif 100<i < 1000:
        if i//100== i%10:
            print(i)
    