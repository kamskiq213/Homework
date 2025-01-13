a = open("9.txt","r")
k=0
for x in a:
    s = [int(m) for m in x.split()]
    povt = [m for m in s if s.count(m) == 2]
    nepovt = [m for m in s if s.count(m) == 1]
    if len(set(povt)) == 2 and len(nepovt) == 3 and (sum(nepovt)/3 <sum(povt)/4):
        k+=1
print(k)
