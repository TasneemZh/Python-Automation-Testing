from selenium import webdriver
from selenium.webdriver.common.by import By

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://en.wikipedia.org/wiki/Main_Page")

links = driver.find_elements(By.TAG_NAME, "a")

for link in links:
    title = link.get_attribute("title")
    if title == "Special:Statistics":
        articles_num = link.get_attribute("innerText")
        break

print(f"Wikipedia Articles Number is {articles_num}")

driver.close()
