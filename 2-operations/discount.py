price = float(input("Введите цену товара: "))
sale =  float(input("Введите процент скидки: "))

price_with_sale = price - ((price * sale) / 100)

print(price_with_sale)