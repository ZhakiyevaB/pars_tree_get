import requests
from bs4 import BeautifulSoup

def parse_olx_page(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "lxml")

    titles = soup.find_all('h6', class_='css-16v5mdi er34gjf0')
    descriptions = soup.find_all('p', class_='css-10b0gli er34gjf0')

    for i, (title, description) in enumerate(zip(titles[:5], descriptions[:5]), start=1):
        title_text = title.text.strip()
        description_text = description.text.strip() if description else "Нет описания"
        print(f"{i}. {title_text}: {description_text}")

def main():
    base_url = "https://www.olx.kz/list/q-елки/"

    for page_num in range(1, 4):  
        url = f"{base_url}?page={page_num}"
        parse_olx_page(url)

main()