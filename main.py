from selenium import webdriver
from fake_useragent import UserAgent
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
options = webdriver.ChromeOptions()
ua = UserAgent()
options.add_argument(f"user-agent={ua.opera}")
options.add_argument("--disable-blink-features=AutomationControlled")
s = Service("C:\\Users\\Evgenii\\PycharmProjects\\selen\\chromedriver\\chromedriver.exe")
driver = webdriver.Chrome(service=s,
                          options=options)


def get_info():
    try:
        driver.get(url="https://www.eldorado.ru/d/smartfony-i-gadzhety/")
        time.sleep(3)
        button_smart = driver.find_element(By.LINK_TEXT, "Смартфоны")
        button_smart.click()
        time.sleep(2)
        apple_click = driver.find_element(By.XPATH, "//*[@title='Apple']")
        apple_click.click()
        time.sleep(2)
        accept_click = driver.find_element(By.XPATH, "//*[text()='Принять']")
        accept_click.click()
        names = driver.find_elements(By.XPATH, "//*[@data-dy='title']")
        prices = driver.find_elements(By.XPATH, "//*[@data-pc='offer_price']")
        v = 1
        dictionary = {}
        for i in range(len(prices)):
            dictionary[str(v) + ' ' + names[i].text] = int(prices[i].text.replace(" ", ""))
            v += 1
        print(dictionary)
        print('min =', min(dictionary.values()))
        print('max =', max(dictionary.values()))
        print('average =', sum(dictionary.values()) / len(dictionary.values()))
    finally:
        driver.close()
        driver.quit()


