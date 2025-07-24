data = []
a = int(input("Введите целое число (0 для окончяния ввода): "))

while a != 0:
    data.append(a)
    a = int(input("Введите целое число (0 для окончяния ввода): "))

data.sort()

print("Числа в порядке возрастания")
for a in data:
    print(a)