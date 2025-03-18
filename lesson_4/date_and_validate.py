import time

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

service = Service(executable_path = ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

driver.get("https://www.youtube.com/")

title_1 = driver.title
print("title", title_1)

driver.get("https://habr.com/ru/articles/784116/")
title_2 = driver.title
print("title", title_2)
driver.back()
current_title = driver.title
assert current_title == title_1, "не та страница"

driver.refresh()

url = driver.current_url
print("Url страницы: ", url)

driver.forward()

url2 = driver.current_url
print("Url страницы: ", url2)
assert url2 == "https://habr.com/ru/articles/784116/", "Not this time"

time.sleep(2)