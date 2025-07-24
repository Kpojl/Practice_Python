coord = input("Введите клетку От a1 До h8: ").lower()
letter, number = coord[0], int(coord[1])

if (ord(letter) - ord('a') + 1 + number) % 2 == 0:
    print("Чёрная")
else:
    print("Белая")