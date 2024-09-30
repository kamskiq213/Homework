rub = int(input("Введите ваше количество денег: "))
price = int(input("Введите цену товара: "))
saleup= int(input("Введите процент увеличения скидки: "))
sale = 5



for i in range(1, int(1e10)):
    if rub >=price:
        rub -= price*(1-sale/100)
        sale = sale + saleup 
        if sale > 99: # чтобы скидка не превысила 99%
            break
        print(f"Остаток денег после {i} покупки: {rub}")
        
    else:
        break