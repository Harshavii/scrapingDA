from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

chrome_driver_path = r'C:\Program Files\chromedriver-win32\chromedriver-win32\chromedriver.exe'  

ser = Service(chrome_driver_path)
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options, service=ser)


website_url = 'https://magicpin.in/New-Delhi/Paharganj/Restaurant/Eatfit/store/61a193/delivery/'  
driver.get(website_url)

# wait for loading site
wait = WebDriverWait(driver, 10)

add = driver.find_element(By.CLASS_NAME, 'add')
add.click()

wait = WebDriverWait(driver, 10)

original_price = driver.find_element(By.XPATH, '//*[@id="merchant-order-summary-react"]/div/div/div[3]/div/button/div[1]/span[1]/span[1]')
print(f"Original Price: {original_price.text}")

final_price = driver.find_element(By.XPATH, '//*[@id="merchant-order-summary-react"]/div/div/div[3]/div/button/div[1]/span[1]/span[2]')
print(f"Final Price: {final_price.text}")


