import requests
from bs4 import BeautifulSoup

def get_net_worth():
    url  = "https://www.forbes.com/profile/jeff-bezos"
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    result = soup.findAll("div", {"class": "profile-info__item-value"})

    if len(result) == 0:
        return None

    return float(result[0].text[1:-1]) * (10 ** 9)

if __name__ == '__main__':
    print(get_net_worth())
