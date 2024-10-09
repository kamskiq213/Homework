st = str(input('Введите строку: '))
st=  list(st)
a = ["а","е","о",'a','e','o']

for b in a:
    while b in st:
        st.remove(b)
print(st)

