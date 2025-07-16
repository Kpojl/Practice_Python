Bread = int(input("Количество вчерашних буханок: "))

BreadPrice = 49 * Bread

Discprice = BreadPrice * 0.6
Totalprice = BreadPrice - Discprice

print("обычная цена: %5.2f" % BreadPrice)
print("цена со скидкой: %5.2f" % Discprice)
print("общая стоимость: %5.2f" % Totalprice)
