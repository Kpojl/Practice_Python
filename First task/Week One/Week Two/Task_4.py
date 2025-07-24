data = []
a = input("Введите слово (оставьте пустую строку для завершения): ")

while a != "":
    if a not in data: 
        data.append(a)
    a = input("Введите слово (оставьте пустую строку для завершения): ")

print("Уникальные слова в порядке ввода:")
for word in data:
    print(word)