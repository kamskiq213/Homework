a = open('part1.txt','r').read()
a = a + '\r'
b = open('part2.txt','r').read()
c = a+b
b = open('full_text.txt','w').write(c)