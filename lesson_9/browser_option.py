import time

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

chrome_options = webdriver.ChromeOptions()
chrome_options.page_load_strategy("eager") # normal - дефолт. игер, как только прогрузился дом, селениум начинает тестировать
#chrome_options.add_argument("--headless")
#chrome_options.add_argument("--incognito")
chrome_options.add_argument("--disable-cache") #отключить кэш
chrome_options.add_argument("--ignore-certificate-errors") #если браузер ругается на сертификаты, а посмотреть очень нужно
#chrome_options.add_argument("--window-size=100.100") # для настройки запускаемого окна
service = Service(executable_path = ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=chrome_options)

driver.set_window_size(1920,1080) #для настройки  окна браузера
driver.get("https://whatismyipaddress.com/")

time.sleep(3)

