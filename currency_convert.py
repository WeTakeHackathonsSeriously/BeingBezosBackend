import requests
from bs4 import BeautifulSoup

def get_conversion_rate():
    url = 'https://www.google.com/search?q="1 usd to gbp"'
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    pound = soup.findAll("span", {"class": "DFlfde SwHCTb"})[0]['data-value']
    return float(pound)

if __name__ == '__main__':
    print(get_conversion_rate())

