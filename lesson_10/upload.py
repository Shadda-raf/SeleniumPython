import time
import os
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

chrome_options = webdriver.ChromeOptions()
service = Service(executable_path = ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=chrome_options)

driver.get("https://demoqa.com/upload-download")
upload_field = driver.find_element("xpath", "//input[@type = 'file']")
upload_field.send_keys(f"{os.getcwd()}\\downloads\\сертификат.jpg")

time.sleep(10)