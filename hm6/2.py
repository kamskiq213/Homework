data = open('data.txt','r').read().split()

new = []
for i in data:
    if int(i) % 2==0:
        new.append(i)
new = ' '.join(new)

data = open('even_numbers.txt','w').write(new)



