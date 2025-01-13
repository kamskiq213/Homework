for n in range(1,101):
    b = bin(n)[2:]
    b1 = b[::-1]
    
    while b1[0] == "0":
        b1 = b1[1:]
    m = int(b1,2)
    if m == 13:
        print(n,m)
        
    
