import requests
from bs4 import BeautifulSoup


def get_product_price(name):
    user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135 Safari/537.36 Edge/12.246'
    headers = {'User-Agent': user_agent}
    url = "https://www.google.com/search?q=\"" + name + "\"&tbm=shop"
    page = requests.get(url, headers=headers)
    soup = BeautifulSoup(page.content, 'html.parser')
    return float(soup.findAll("span", {"class": "Nr22bf"})[0].text[1:-1])

if __name__ == '__main__':
    print(get_product_price("lamp"))
