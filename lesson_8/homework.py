import time

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

service = Service(executable_path = ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

#1st part

driver.get("https://demoqa.com/text-box")
time.sleep(10)

full_name_input = driver.find_element("xpath", "//input[@placeholder = 'Full Name']")
full_name_input.clear()
full_name_input.send_keys("Konstanin Mumuev")
assert full_name_input.get_attribute("value") == "Konstanin Mumuev", "В поле ввода информация не совпадет с вводимой в тесте"

email_input = driver.find_element("xpath", "//input[@id = 'userEmail']")
email_input.clear()
email_input.send_keys("QAQA@qa.qa")
assert email_input.get_attribute("value")  == "QAQA@qa.qa", "В поле ввода имейла информация не совпадает с вводимой в тексте"

current_address_textarea = driver.find_element("xpath", "//textarea[@id = 'currentAddress']")
current_address_textarea.clear()
current_address_textarea.send_keys("Armenia, Erevan, Tigran Mets street, 8/78")
assert current_address_textarea.get_attribute("value")  == "Armenia, Erevan, Tigran Mets street, 8/78", "В поле ввода текущего адреса информация не совпадает с вводимой в тексте"

permanent_address_textarea = driver.find_element("xpath", "//textarea[@id = 'permanentAddress']")
permanent_address_textarea.clear()
permanent_address_textarea.send_keys("Armenia, Erevan, Tigran Mets street, 8/78")
assert permanent_address_textarea.get_attribute("value")  == "Armenia, Erevan, Tigran Mets street, 8/78", "В поле ввода постоянного адреса информация не совпадает с вводимой в тексте"

#2nd part

start_page = "https://the-internet.herokuapp.com/status_codes"
driver.get(start_page)
time.sleep(5)

links= driver.find_elements("xpath", "//li/a")
li_count = len(links)

for status_code in links:
    status_code_text = status_code.get_attribute("text")
    status_code.click()
    status_code_url = driver.current_url
    assert f"{start_page}/{status_code_text}" == status_code_url , f"URL'ы не совпадают для статус кода № {status_code_text}"
    driver.back()
    assert start_page == driver.current_url,"Возврат был совершен не на стартовую страницу"