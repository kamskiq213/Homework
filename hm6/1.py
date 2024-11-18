with open('text.txt', 'r', encoding='utf-8') as file:
    data = file.read()

char = len(data.replace('\n', ''))

words= len(data.split())
lines = data.count('\n')

print(f'Количество символов: {char}')
print(f'Количество слов: {words}')
print(f'Количество строк: {lines}')
print(list(data))
