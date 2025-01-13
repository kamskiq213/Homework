from itertools import *
k=0

for x in permutations("ГАГАГАГ",7):
    s = "".join(x)
    if s.count("АА") == 0 and  s.count("ГГ")==0:
        k+=1
print(k)
    
