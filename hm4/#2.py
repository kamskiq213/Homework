n = int(input("Введите число n : "))
a = int(input("Введите число a : "))
r = int(input("Введите число r : "))    

for i in range(1, n+1):
    print(a * (r **(i-1)))