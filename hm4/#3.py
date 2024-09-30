chet = 0
nechet = 0
a  = int(input("Введите кол-во чисел: "))

for i in range(a):
    b = int(input("Введите число: "))
    if b % 2 == 0:
        chet += 1
    else:
        nechet += 1
print(f"Кол-во четных чисел: {chet}")
print(f"Кол-во нечетных чисел: {nechet}")