import requests
from bs4 import BeautifulSoup
import csv

url = "https://magicpin.in/New-Delhi/Paharganj/Restaurant/Eatfit/store/61a193/delivery/"

response = requests.get(url)

data = []
unique_items = set()

# scraping data
if response.status_code == 200:
    soup = BeautifulSoup(response.text, 'html.parser')

    menu_items = soup.find_all('article', {'class': 'itemInfo'})

# removing duplicate values
    for item in menu_items:
        name = item.find('a', {'class': 'itemName'}).text.strip()
        price = item.find('span', {'class': 'itemPrice'}).text.strip()

        if name not in unique_items:
            unique_items.add(name)
            data.append([name, price])

    headers = ["Menu Name", "Menu Price"]

# storing data in csv file
    csv_filename = "scraped_data.csv"
    with open(csv_filename, 'w', newline='', encoding='utf-8') as csvfile:
        csv_writer = csv.writer(csvfile)
        csv_writer.writerow(headers)
        csv_writer.writerows(data)

    print(f"\nData has been saved to {csv_filename}")

else:
    print("Failed to retrieve the page. Status code:", response.status_code)
