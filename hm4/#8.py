count = int(input('Введите количество участков: '))

time = 0

for i in range(count):
    s = int(input(f'Введите длину участка в км {i+1}: '))
    v = int(input(f'Введите среднюю скорость на участке в км/ч {i+1}: '))
    time+=s/v
print(f'Время поездки: {time} часов')