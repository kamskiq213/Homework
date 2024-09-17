sum=0
sum13=0
for i in range(int(1000000)):
    num1= int(i % 10)
    num2 = int((i % 100) // 10)
    num3 = int((i % 1000) // 100)
    num4 = int((i // 1000) % 10)
    num5 = int((i // 10000) % 10)
    num6 = int((i // 100000) % 10)

    #print(f'{num3}{num2}{num1}{num4}{num5}{num6}')
    if num1 + num2 + num3 == num4 + num5 + num6:
        sum += 1
    if num1 + num2 + num3 + num4 + num5 + num6 == 13:
        sum13 += 1
print(f'Число счастливых билетов : {sum}')
print(f'Число счастливых билетов с суммой 13 : {sum13}')
        