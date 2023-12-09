import requests
from bs4 import BeautifulSoup
from tabulate import tabulate

url = "https://magicpin.in/New-Delhi/Paharganj/Restaurant/Eatfit/store/61a193/delivery/"

response = requests.get(url)

data=[]

if response.status_code == 200:
    soup = BeautifulSoup(response.text, 'html.parser')

    menu_items = soup.find_all('article', {'class': 'itemInfo'})

    for item in menu_items:
        name = item.find('a', {'class': 'itemName'}).text.strip()
        # print(name)
        price = item.find('span', {'class': 'itemPrice'}).text.strip()
        # print(price)

        data.append([name, price])

        headers = ["Menu Name", "Menu Price"]
        print(tabulate(data, headers, tablefmt="plain"))
        # print(f"{name}: {price}")

else:
    print("Failed to retrieve the page. Status code:", response.status_code)
