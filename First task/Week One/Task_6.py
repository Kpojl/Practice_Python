Bread = int(input("Количество вчерашних буханок: "))

Bread_Price = 49 * Bread
Disc_price = Bread_Price * 0.6
Total_price = Bread_Price - Disc_price

print("обычная цена: %5.2f" % Bread_Price)
print("цена со скидкой: %5.2f" % Disc_price)
print("общая стоимость: %5.2f" % Total_price)