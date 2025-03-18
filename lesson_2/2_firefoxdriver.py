from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.chrome.service import Service

service = Service(executable_path = GeckoDriverManager().install())
driver = webdriver.Firefox(service=service)