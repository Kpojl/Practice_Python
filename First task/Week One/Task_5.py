monet = int(input("Введите сумму сдачи в копейках: "))

Fiverub = monet // 500
remaining = monet % 500

Tworub = remaining // 200
remaining %= 200

Onerub = remaining // 100
remaining %= 100

FivTinkop = remaining // 50
remaining %= 50

kop10 = remaining // 10
remaining %= 10

kop5 = remaining // 5
remaining %= 5

kop1 = remaining  

print("5 руб:", Fiverub)
print("2 руб:", Tworub)
print("1 руб:", Onerub)
print("50 копеек:", FivTinkop)
print("10 копеек:", kop10)
print("5 копеек:", kop5)
print("1 копеек:", kop1)