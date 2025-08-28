import requests
from bs4 import BeautifulSoup

def scrape_ai_news():
    """
    Скрейпинг новостей ИИ с сайта 2051.vision
    """
    url = "https://2051.vision/category/ii/"
    
    try:

        response = requests.get(url)
        response.raise_for_status()  
        

        soup = BeautifulSoup(response.text, 'html.parser')
        

        news_titles = []
        

        selectors = [
            'h1 a', 'h2 a', 'h3 a',  
            '.entry-title a', '.post-title a', '.title a',  
            'article h2 a', '.news-item h3 a'  
        ]
        
        for selector in selectors:
            titles = soup.select(selector)
            if titles:
                print(f"Найдено заголовков с селектором '{selector}': {len(titles)}")
                for title in titles:
                    news_text = title.get_text(strip=True)
                    if news_text and len(news_text) > 10:  
                        news_titles.append(news_text)
                break
        
        
        if not news_titles:
            print("Поиск альтернативными методами...")
            # Ищем все ссылки с текстом
            all_links = soup.find_all('a')
            for link in all_links:
                text = link.get_text(strip=True)
                if text and len(text) > 20 and len(text) < 200:  
                    news_titles.append(text)
        
        
        print("\n" + "="*60)
        print(f"НОВОСТИ ИИ С САЙТА 2051.VISION")
        print("="*60)
        
        if news_titles:
            for i, title in enumerate(news_titles[:15], 1):  
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