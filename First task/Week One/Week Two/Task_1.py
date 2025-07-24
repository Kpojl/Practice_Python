a = float(input("Введите ваш ваозраст: "))

one_year = 10.5
two_year = 10.5
other_year = 4.0
total = 0.0

if a <= 0:
    total = 0
elif a <= 1:
    total = one_year
elif a <= 2:
    total = one_year + two_year
else:
    total = one_year + two_year + (other_year * (a - 2))

print("Возраст собки:", total)