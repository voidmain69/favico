import pandas as pd
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

def find_favicon_url(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    # Опции rel, которые могут содержать URL favicon
    rel_options = ['icon', 'shortcut icon', 'apple-touch-icon', 'apple-touch-icon-precomposed']
    favicon_tag = soup.find('link', rel=lambda value: value and value.lower() in rel_options)

    if favicon_tag:
        favicon_url = favicon_tag['href']
        favicon_url = urljoin(url, favicon_url)
        return favicon_url
    else:
        return None

def main():
    # Загрузка данных из Excel
    excel_file_path = 'sites.xlsx'
    df = pd.read_excel(excel_file_path)

    # Добавление нового столбца 'favIco'
    df['favIco'] = df['urls'].apply(lambda url: find_favicon_url(url) if pd.notna(url) else None)

    # Сохранение изменений обратно в Excel
    df.to_excel(excel_file_path, index=False)

    print("Favicon URLs добавлены в столбец 'favIco'.")

if __name__ == "__main__":
    main()
