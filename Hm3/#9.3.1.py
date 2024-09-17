stipendia = int(input('Стипендия в месяц: '))
rashodi = int(input('Расходы в месяц(должны быть больше стипендии): '))
months = int(input('Сколько месяцев хотим прожить: '))

sum = 0

for i in range(1, months+1):
    sum+=rashodi - stipendia 
print(f'Начальная сумма денег которая должна быть: {sum} руб.')