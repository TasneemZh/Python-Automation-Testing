from selenium import webdriver
from dotenv import load_dotenv
from login import login_into_linkedin
from search import search_for_job

load_dotenv(".env")

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://www.linkedin.com/login")

login_into_linkedin(driver)
search_for_job(driver)

driver.close()
