data = []

while True:
    user_input = input("Введите целое число (0 для окончания ввода): ")
    if user_input == "0":
        break
    try:
        data.append(int(user_input))
    except ValueError:
        print("Ошибка! Введите целое число.")

data.sort()
print("\nЧисла в порядке возрастания:")
print(*data, sep="\n")  # Красивый вывод