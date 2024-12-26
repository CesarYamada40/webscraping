import requests
from bs4 import BeautifulSoup

def scrape_data():
    url = 'https://www.seusite.com'  # Substitua pela URL real que você deseja extrair
    response = requests.get(url)
    
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Exemplo: extrair todos os títulos de artigos
        titles = [title.text for title in soup.find_all('h2')]  # Altere 'h2' conforme necessário
        
        # Exemplo: extrair todos os parágrafos
        paragraphs = [p.text for p in soup.find_all('p')]  # Altere 'p' conforme necessário
        
        return {
            'titles': titles,
            'paragraphs': paragraphs
        }
    else:
        return {'error': 'Failed to retrieve data'}