while True:
    num = input("Введите число (Enter для завершения): ")
    if num == "":
        break
    numbers.append(float(num))

# Проверка на пустой список
if not numbers:
    print("Вы не ввели ни одного числа!")
else:
    # Вычисление среднего
    avg = sum(numbers) / len(numbers)
    print(f"\nСреднее значение: {avg:.2f}")

    # Разделение чисел
    below = []
    equal = []
    above = []
    
    for num in numbers:
        if num < avg:
            below.append(num)
        elif num == avg:
            equal.append(num)
        else:
            above.append(num)

    # Вывод результатов
    print("\nЧисла ниже среднего:", ', '.join(map(str, below)))
    print("Числа равные среднему:", ', '.join(map(str, equal)))
    print("Числа выше среднего:", ', '.join(map(str, above)))