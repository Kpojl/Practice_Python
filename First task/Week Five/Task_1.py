import os

def create_test_file():
    """Создает тестовый файл если он не существует"""
    test_content = """The quick brown fox jumps over the lazy dog.
Hello world! This is a test example.
Programming is fun. Python is awesome.
Statistics and analysis of letter usage.
Gadsby was written without the letter E."""

    with open('Test.txt', 'w', encoding='utf-8') as f:
        f.write(test_content)
    print("✅ Создан тестовый файл Test.txt")

def analyze_letters_simple(filename):
    # Сначала проверим существует ли файл
    if not os.path.exists(filename):
        print(f"❌ Файл '{filename}' не найден!")
        create = input("Создать тестовый файл? (y/n): ")
        if create.lower() == 'y':
            create_test_file()
            filename = 'Test.txt'  # Теперь анализируем созданный файл
        else:
            return False
    
    # Остальной код без изменений
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
                    clean_word = word.upper().rstrip('.,!?;:"()')
                    clean_word = ''.join(char for char in clean_word if char.isalpha())
                    
                    if clean_word:
                        total_words += 1
                        for letter in set(clean_word):
                            if letter in counts:
                                counts[letter] += 1
    
    except Exception as e:
        print(f"❌ Ошибка при чтении файла: {e}")
        return False
    
    # Выводим статистику
    print(f"📊 Всего проанализировано слов: {total_words}")
    print()
    print("Буква : Слов   %")
    print("-" * 18)
    
    for letter in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
        percentage = (counts[letter] / total_words * 100) if total_words > 0 else 0
        print(f"{letter}     : {counts[letter]:4d}  {percentage:6.2f}%")
    
    min_count = min(counts.values())
    rarest = [letter for letter, count in counts.items() if count == min_count]
    
    print(f"\n🎯 Самая редкая буква: {', '.join(rarest)} (встречается в {min_count} словах)")
    return True

def main():
    print("=" * 50)
    print("АНАЛИЗАТОР СТАТИСТИКИ БУКВ В СЛОВАХ")
    print("=" * 50)
    
    while True:
        print("\nВыберите вариант:")
        print("1 - Проанализировать файл Test.txt")
        print("2 - Ввести другое имя файла")
        print("3 - Показать текущую папку")
        print("4 - Выйти из программы")
        
        choice = input("Ваш выбор (1/2/3/4): ").strip()
        
        if choice == '1':
            analyze_letters_simple('Test.txt')
        
        elif choice == '2':
            filename = input("Введите имя файла: ").strip()
            if filename:
                analyze_letters_simple(filename)
        
        elif choice == '3':
            print(f"📁 Текущая папка: {os.getcwd()}")
            print("Файлы в папке:")
            for file in os.listdir('.'):
                if os.path.isfile(file):
                    print(f"  📄 {file}")
        
        elif choice == '4':
            print("👋 До свидания!")
            break
        
        else:
            print("❌ Неверный выбор. Попробуйте снова.")
        
        if choice in ['1', '2']:
            input("\nНажмите Enter для продолжения...")

if __name__ == "__main__":
    main()