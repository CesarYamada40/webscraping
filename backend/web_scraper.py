import requests
from bs4 import BeautifulSoup

def scrape_data(query):
    # Formatar a URL corretamente
    url = f'https://g1.com.br/busca?q={query}'  # URL de busca correta
    try:
        response = requests.get(url)
        response.raise_for_status()  # Levanta um erro para códigos de status HTTP 4xx e 5xx

        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Exemplo: extrair todos os títulos de artigos
        titles = [title.text for title in soup.find_all('h2')]  # Altere 'h2' conforme necessário
        
        # Exemplo: extrair todos os parágrafos
        paragraphs = [p.text for p in soup.find_all('p')]  # Altere 'p' conforme necessário
        
        return {
            'titles': titles,
            'paragraphs': paragraphs
        }
    except requests.exceptions.RequestException as e:
        return {'error': f'Failed to retrieve data: {e}'}