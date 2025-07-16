souvenir = int(input("Введите колличество сувениров: "))
trinket = int(input("Введите колличество безделушек: "))

souvenirWeight = (souvenir * 75)
trinketWeight = (trinket * 112)

total = souvenirWeight + trinketWeight

print("Общий вес посылки",total)
