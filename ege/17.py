s = open("17.txt","r")

a = [int(x) for x in s]

p = 0
psum=[]
for i in range(0,len(a)):
    p
    if (a[i] * a[i+1]) % 15 == 0 and (a[i] + a[i+1]) % 7 == 0:
        psum.append(int(a[i])+int(a[i+1]))
        p+=1
print(p)
print(max(psum))
         
