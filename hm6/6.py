a = open('message.txt','r',encoding='UTF-8').read()
print(a)
letters = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
print(a.find('п')+3)

for i in a:
    if i in letters:
        n = letters.find(i) +3
        print(letters.find(i))
        print(n)
        a =a.replace(i,letters[n])


b = open('encrypted_message.txt','w',encoding='UTF-8').write(a)
