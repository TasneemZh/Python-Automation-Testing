import os
from selenium.webdriver.common.by import By
from dotenv import load_dotenv

load_dotenv(".env")


def login_into_linkedin(driver):
    email_element = driver.find_element(By.ID, "username")
    password_element = driver.find_element(By.ID, "password")

    email_element.send_keys(os.environ.get("USER_EMAIL"))
    password_element.send_keys(os.environ.get("USER_PASSWORD"))

    button_element = driver.find_element(By.XPATH, "//button[@type='submit']")
    button_element.click()
