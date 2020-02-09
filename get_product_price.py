import requests
from bs4 import BeautifulSoup


def get_product_price(name):
    user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135 Safari/537.36 Edge/12.246'
    headers = {'User-Agent': user_agent}
    url = "https://www.google.com/search?q=\"" + name + "\"&tbm=shop"
    page = requests.get(url, headers=headers)
    soup = BeautifulSoup(page.content, 'html.parser')
    results = soup.findAll("span", {"class": "Nr22bf"})

    price = 0
    n = min(4, len(results))

    if n == 0:
        return None

    for i in range(n):
        price += float(results[i].text.replace(',','')[1:-1])
    return price / (n - 1)


if __name__ == '__main__':
    print(get_product_price("jeff bezos"))
