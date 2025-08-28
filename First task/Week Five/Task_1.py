def analyze_letter_statistics(filename):
    counts = {}
    for ch in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
        counts[ch] = 0
    
    total_words = 0
    
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            for line in file:
                words = line.split()
                for word in words:
                    clean_word = ''.join(char for char in word if char.isalpha()).upper()
                    
                    if clean_word:  
                        total_words += 1
                        
                        
                        unique_letters_in_word = set(clean_word)
                        for letter in unique_letters_in_word:
                            if letter in counts:
                                counts[letter] += 1
    
    except FileNotFoundError:
        print(f"Ошибка: Файл '{filename}' не найден.")
        return
    
    percentages = {}
    for letter, count in counts.items():
        if total_words > 0:
            percentages[letter] = (count / total_words) * 100
        else:
            percentages[letter] = 0
    
    smallest_count = min(counts.values())
    rarest_letters = [letter for letter, count in counts.items() if count == smallest_count]
    
    print("Статистика использования букв в словах:")
    print("=" * 50)
    print(f"Всего проанализировано слов: {total_words}")
    print()
    
    sorted_letters = sorted(counts.keys())
    for letter in sorted_letters:
        print(f"{letter}: {counts[letter]:4d} слов ({percentages[letter]:6.2f}%)")
    
    print()
    print("Наиболее редко встречающаяся буква(ы):")
    for letter in rarest_letters:
        print(f"{letter}: {counts[letter]} слов ({percentages[letter]:.2f}%)")

if __name__ == "__main__":
    test_content = """The quick brown fox jumps over the lazy dog.
Hello world! This is a test example.
Programming is fun. Python is awesome.
Statistics and analysis."""
    
    with open('test_words.txt', 'w', encoding='utf-8') as f:
        f.write(test_content)
    
    analyze_letter_statistics('test_words.txt')