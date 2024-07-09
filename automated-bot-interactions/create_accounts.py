from selenium import webdriver
from selenium.webdriver.common.by import By

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://secure-retreat-92358.herokuapp.com/")

first_name = driver.find_element(By.NAME, "fName")
last_name = driver.find_element(By.NAME, "lName")
email = driver.find_element(By.NAME, "email")

first_name.send_keys("Test")
last_name.send_keys("Userr")
email.send_keys("test@example.com")

buttons = driver.find_elements(By.TAG_NAME, "button")
for button in buttons:
    value = button.get_attribute("type")
    if value == "submit":
        button.click()
        break

driver.close()
