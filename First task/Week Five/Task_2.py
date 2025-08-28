import requests
from bs4 import BeautifulSoup

def scrape_ai_news():
    """
    Скрейпинг новостей ИИ с сайта 2051.vision
    """
    url = "https://2051.vision/category/ii/"
    
    try:
        # Отправляем GET-запрос к сайту
        response = requests.get(url)
        response.raise_for_status()  # Проверяем успешность запроса
        
        # Создаем объект BeautifulSoup для парсинга HTML
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Ищем все заголовки новостей
        # Анализируем структуру страницы для поиска правильных селекторов
        news_titles = []
        
        # Попробуем несколько возможных селекторов для заголовков
        # Обычно заголовки находятся в тегах h1-h3 с классами
        selectors = [
            'h1 a', 'h2 a', 'h3 a',  # заголовки с ссылками
            '.entry-title a', '.post-title a', '.title a',  # распространенные классы
            'article h2 a', '.news-item h3 a'  # типичные структуры
        ]
        
        for selector in selectors:
            titles = soup.select(selector)
            if titles:
                print(f"Найдено заголовков с селектором '{selector}': {len(titles)}")
                for title in titles:
                    news_text = title.get_text(strip=True)
                    if news_text and len(news_text) > 10:  # Фильтруем короткие тексты
                        news_titles.append(news_text)
                break
        
        # Если не нашли через селекторы, попробуем другой подход
        if not news_titles:
            print("Поиск альтернативными методами...")
            # Ищем все ссылки с текстом
            all_links = soup.find_all('a')
            for link in all_links:
                text = link.get_text(strip=True)
                if text and len(text) > 20 and len(text) < 200:  # Предполагаем, что заголовки средней длины
                    news_titles.append(text)
        
        # Выводим результаты
        print("\n" + "="*60)
        print(f"НОВОСТИ ИИ С САЙТА 2051.VISION")
        print("="*60)
        
        if news_titles:
            for i, title in enumerate(news_titles[:15], 1):  # Выводим первые 15 заголовков
                print(f"{i}. {title}")
        else:
            print("Не удалось найти заголовки новостей.")
            print("Возможные причины:")
            print("- Изменилась структура сайта")
            print("- Требуется обновление селекторов")
            print("- Сайт использует JavaScript для загрузки контента")
            
    except requests.exceptions.RequestException as e:
        print(f"Ошибка при запросе к сайту: {e}")
    except Exception as e:
        print(f"Произошла ошибка: {e}")

# Запуск скрейпинга
if __name__ == "__main__":
    scrape_ai_news()