from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BingSearchBox:
    driver = None

    def __init__(self, driver):
        self.driver = driver

    def search_term(self, hotel_name, city):
        search_box = self.driver.find_element(By.ID, "sb_form_q")
        search_box.send_keys(hotel_name + " " + city + " expedia")

    def submit_search(self):
        self.driver.execute_script("document.getElementById('sb_form_go').click()")
        # search_button = WebDriverWait(self.driver, 10).until(
        #     EC.presence_of_element_located((By.ID, "sb_form_go"))
        # )
        # search_button.click()
