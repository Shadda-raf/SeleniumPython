import time

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

service = Service(executable_path = ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

driver.get("https://testautomationpractice.blogspot.com/")
time.sleep(5)

icon_wiki = driver.find_element("class name", "wikipedia-icon")
assert icon_wiki.get_attribute("src") ==  "https://resources.blogblog.com/img/widgets/icon_wikipedia_w.png", "не та картинка"

search_input_wiki =  driver.find_element("id", "Wikipedia1_wikipedia-search-input")
assert search_input_wiki.get_attribute("class") == "wikipedia-search-input", "это не поле ввода Википедии"

search_button = driver.find_element("class name", "wikipedia-search-button")
assert search_button.get_attribute("type") == "submit", "это не лупа"
prompt_button = driver.find_elements("tag name", "BUTTON")[6]
assert prompt_button.get_attribute("id") == "promptBtn", "Это не кнопка ввода"
