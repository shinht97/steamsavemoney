from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options as ChromeOptions
from webdriver_manager.chrome import ChromeDriverManager
from selenium.common.exceptions import NoSuchElementException, StaleElementReferenceException

import pandas as pd
import time
import datetime

options = ChromeOptions()

user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36"

options.add_argument(f"user-agent={user_agent}")
options.add_argument("lang=ko_KR")
# options.add_argument("headless")  # 실제 웹 페이지 띄우지 않음
# options.add_argument("window-size=1920X1080")  # 웹 창 크기 지정

service = ChromeService(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=options)

start_url = "https://store.steampowered.com/search/?filter=topsellers"

driver.get(start_url)

time.sleep(1)

btn_language_xpath = '//*[@id="language_pulldown"]'
btn_language = driver.find_element(By.XPATH, btn_language_xpath)
driver.execute_script("arguments[0].click();", btn_language)
time.sleep(1)

btn_korean_xpath = '//*[@id="language_dropdown"]/div/a[4]'
btn_korean = driver.find_element(By.XPATH, btn_korean_xpath)
driver.execute_script("arguments[0].click();", btn_korean)
time.sleep(1)

for i in range(27):
    print(f"\r스크롤 {i+1}번째", end="")
    driver.execute_script("window.scrollTo(0, document.documentElement.scrollHeight);")  # 스크롤 내리는 동작
    time.sleep(3)

print("\r스크롤 끝")

game_links = []
game_titles = []
reviews_links = []

for i in range(1, 1001):
    if i % 10 == 0:
        print(f"\r링크 따는 중 {i/1001 * 100}%", end="")

    game_link = driver.find_element(By.XPATH, f'//*[@id="search_resultsRows"]/a[{i}]').get_attribute("href")
    game_links.append(game_link)

    game_title = driver.find_element(By.XPATH, f'//*[@id="search_resultsRows"]/a[{i}]/div[2]/div[1]/span').text
    game_titles.append(game_title)

    game_code = game_link.split("/")[4]
    review_link = f"https://steamcommunity.com/app/{game_code}/reviews/?filterLanguage=koreana"
    reviews_links.append(review_link)

print("\r링크 작업 끝")

print(game_links[:5])
print(len(game_links))

print(game_titles[:5])
print(len(game_titles))

print(reviews_links[:5])
print(len(reviews_links))

df = pd.DataFrame({"titles": game_titles, "gamelinks": game_links, "reviewlinks": reviews_links})

df.to_csv("../steam.csv", index=False)
