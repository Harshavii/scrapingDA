import requests
import random
from requests.exceptions import ProxyError, SSLError

def get_proxies():

    proxies = ['http://103.44.116.22:3128', 'http://103.41.90.17:83', 'http://139.59.1.14:3128', 'http://103.39.247.205:8080', 'http://103.85.102.10:82', 'http://121.240.127.86:8081', 'http://115.96.208.124:8080']
    return proxies

def scrape_page(url, proxy):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'}

    try:
        response = requests.get(url, headers=headers, proxies=proxy, timeout=20)
        response.raise_for_status()
    except (ProxyError, SSLError):
        print('Proxy failed.')
        return None
    except requests.exceptions.HTTPError as errh:
        print("HTTP Error:", errh)
        return None
    except requests.exceptions.ConnectionError as errc:
        print("Error Connecting:", errc)
        return None
    except requests.exceptions.Timeout as errt:
        print("Timeout Error:", errt)
        return None
    except requests.exceptions.RequestException as err:
        print("Something went wrong:", err)
        return None

    return response.text

def scrape_multiple_pages(urls, proxies):
    results = []
    for url in urls:
        proxy = {'http': random.choice(proxies)}
        response = scrape_page(url, proxy)
        if response:
            results.append(response)
    return results

proxies = get_proxies()
urls = ['https://magicpin.in/', 'https://www.amazon.in/']

results = scrape_multiple_pages(urls, proxies)

for i, result in enumerate(results):
    with open(f'page{i+1}.html', 'w', encoding='utf-8') as f:
        f.write(result)