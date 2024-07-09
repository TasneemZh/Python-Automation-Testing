from datetime import datetime
from selenium import webdriver
from selenium.webdriver.common.by import By

events_dict = {}
cnt = 0

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://www.python.org/")

title_element = driver.find_element(By.XPATH, "//*[@class='icon-calendar']/..")
title = title_element.get_attribute("innerText")
li_elements = driver.find_elements(By.XPATH, "//*[@class='icon-calendar']/../../ul[@class='menu']/li")

for li in li_elements:
    time_element = li.find_element(By.TAG_NAME, "time")
    date = time_element.get_attribute("datetime")
    year = datetime.fromisoformat(date).year
    month = datetime.fromisoformat(date).month
    day = datetime.fromisoformat(date).day
    ref_element = li.find_element(By.TAG_NAME, "a")
    event_name = ref_element.get_attribute("innerHTML")
    events_dict[cnt] = {"date": f"{year}-{month}-{day}", "event": event_name}
    cnt += 1

print(f"{title}: {events_dict}")
driver.close()
