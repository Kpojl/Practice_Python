import math

OneNumber = int(input("Введите первое число:"))
TwoNumber = int(input("Введите второе число:"))

sum = OneNumber + TwoNumber
minus = OneNumber - TwoNumber
multi = OneNumber * TwoNumber
deli = OneNumber / TwoNumber
ost = OneNumber % TwoNumber
loga = math.log10(OneNumber)
step = OneNumber ** TwoNumber

print("Сумма Первого и Второго числа:",sum)
print("Разность Первого и Второго числа:",minus)
print("Произведение Первого и Второго числа:",multi)
print("Частное от деления Первого и Второго числа:",deli)
print("Остаток от деления Первого и Второго числа:",ost)
print("Логарифм Первого числа:",loga)
print("Возведение Первого числа в степень Второго числа:",step)