import time

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

service = Service(executable_path = ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

driver.get("https://yandex.ru") #переход по ссылке

time.sleep(10) #задержка до закрытия окна. время в секундах

driver.back() #навигация. нажатие на кнопку браузера назад;
driver.forward() #навигация. нажатие на кнопку браузера вперед;
driver.refresh() #F5