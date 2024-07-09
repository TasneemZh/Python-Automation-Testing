from selenium import webdriver
from selenium.webdriver.common.by import By
import time

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://orteil.dashnet.org/experiments/cookie/")

cookie_element = driver.find_element(By.ID, "cookie")

start_time = time.time()  # remember when we started
while (time.time() - start_time) < 5:  # keep clicking for 5 seconds
    try:
        cookie_element.click()
    except Exception as e:
        print("Error: ", e)
        break

driver.close()
