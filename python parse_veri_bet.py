import requests
from bs4 import BeautifulSoup
from dataclasses import dataclass
import json

@dataclass
class Item:
    sport_league: str = ''
    event_date_utc: str = ''
    team1: str = ''
    team2: str = ''
    pitcher: str = ''
    period: str = ''
    line_type: str = ''
    price: str = ''
    side: str = ''
    team: str = ''
    spread: float = 0.0

def parse_veri_bet():
    url = "https://veri.bet/simulator"
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"}

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        items = []

        # A lógica de extração dos dados depende da estrutura específica da página, atualize conforme necessário.
        # Aqui é um exemplo genérico:

        # Obter todos os elementos que contêm informações sobre as apostas
        bet_elements = soup.find_all("div", class_="bet-info")

        for bet_element in bet_elements:
            item = Item()
            # Preencher os campos do item com os dados extraídos
            item.sport_league = "NFL"  # Substitua com a lógica para obter o nome da liga
            item.event_date_utc = bet_element.find("span", class_="event-time")["data-utc"]
            item.team1 = bet_element.find("span", class_="team-name team1").text.strip()
            item.team2 = bet_element.find("span", class_="team-name team2").text.strip()
            item.period = bet_element.find("span", class_="period").text.strip()
            item.price = bet_element.find("span", class_="price").text.strip()
            item.line_type = bet_element.find("span", class_="line-type").text.strip()
            item.side = bet_element.find("span", class_="side").text.strip()
            item.team = bet_element.find("span", class_="team").text.strip()

            # Adicione o item à lista
            items.append(item)

        # Converter a lista de itens para JSON e imprimir no console
        json_data = json.dumps([item.__dict__ for item in items], indent=2)
        print(json_data)

if __name__ == "__main__":
    parse_veri_bet()