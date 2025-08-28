def analyze_letters_simple(filename):
    # Инициализируем счетчики
    counts = {}
    for ch in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
        counts[ch] = 0
    
    total_words = 0
    
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            print(f"📖 Анализируем файл: {filename}")
            print("-" * 40)
            
            for line in file:
                words = line.split()
                for word in words:
                    # Очищаем слово и переводим в верхний регистр
                    clean_word = word.upper().rstrip('.,!?;:"()')
                    clean_word = ''.join(char for char in clean_word if char.isalpha())
                    
                    if clean_word:
                        total_words += 1
                        # Отмечаем все буквы, которые есть в этом слове
                        for letter in set(clean_word):
                            if letter in counts:
                                counts[letter] += 1
    
    except FileNotFoundError:
        print(f"❌ Ошибка: Файл '{filename}' не найден!")
        print("Проверьте:")
        print("1. Правильно ли указано имя файла")
        print("2. Находится ли файл в той же папке, что и программа")
        print("3. Для файла в другой папке укажите полный путь")
        return False
    except PermissionError:
        print(f"❌ Ошибка: Нет доступа к файлу '{filename}'")
        return False
    except Exception as e:
        print(f"❌ Произошла непредвиденная ошибка: {e}")
        return False
    
    # Проверяем, есть ли слова для анализа
    if total_words == 0:
        print("⚠️ В файле не найдено подходящих слов для анализа")
        return False
    
    # Выводим статистику
    print(f"📊 Всего проанализировано слов: {total_words}")
    print()
    print("Буква : Слов   %")
    print("-" * 18)
    
    for letter in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
        percentage = (counts[letter] / total_words * 100) if total_words > 0 else 0
        print(f"{letter}     : {counts[letter]:4d}  {percentage:6.2f}%")
    
    # Находим самую редкую букву
    min_count = min(counts.values())
    rarest = [letter for letter, count in counts.items() if count == min_count]
    
    print(f"\n🎯 Самая редкая буква: {', '.join(rarest)} (встречается в {min_count} словах)")
    return True

# Основная программа с выбором файла
def main():
    print("=" * 50)
    print("АНАЛИЗАТОР СТАТИСТИКИ БУКВ В СЛОВАХ")
    print("=" * 50)
    
    while True:
        print("\nВыберите вариант:")
        print("1 - Проанализировать файл Test.txt")
        print("2 - Ввести другое имя файла")
        print("3 - Выйти из программы")
        
        choice = input("Ваш выбор (1/2/3): ").strip()
        
        if choice == '1':
            # Анализ файла Test.txt
            analyze_letters_simple('Test.txt')
        
        elif choice == '2':
            # Ввод собственного имени файла
            filename = input("Введите имя файла: ").strip()
            if filename:
                analyze_letters_simple(filename)
            else:
                print("❌ Имя файла не может быть пустым!")
        
        elif choice == '3':
            print("👋 До свидания!")
            break
        
        else:
            print("❌ Неверный выбор. Попробуйте снова.")
        
        # Пауза перед следующим выбором
        if choice in ['1', '2']:
            input("\nНажмите Enter для продолжения...")

# Запуск программы
if __name__ == "__main__":
    main()