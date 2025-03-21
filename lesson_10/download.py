import time
import os
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

chrome_options = webdriver.ChromeOptions()
prefs = {
    "download.default_directory" : f"{os.getcwd()}\\download",
    "safebrowsing.enabled" : False
}
chrome_options.add_experimental_option("prefs", prefs)
service = Service(executable_path = ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=chrome_options)

driver.get("https://the-internet.herokuapp.com/download")

time.sleep(3)
files_for_dl = driver.find_elements("xpath", "//a")
for file_for_dl in files_for_dl:
    try:
        file_for_dl.click()
    except:
        continue

time.sleep(4)
