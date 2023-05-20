from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class ButtonsClick:
    driver = None

    def __init__(self, driver):
        self.driver = driver

    def click_on_button_by_id(self, button_id):
        hyperlinked_button = self.driver.find_element(By.ID, button_id)
        hyperlinked_button.click()

    def click_hyperlinked_buttons(self, button_substring):
        header_button = WebDriverWait(self.driver, 20).until(
            EC.visibility_of_element_located((By.PARTIAL_LINK_TEXT, button_substring)))
        header_button.click()

    def click_on_button_by_xpath(self, xpath):
        WebDriverWait(self.driver, 35).until(
            EC.element_to_be_clickable((By.XPATH, xpath)))
        button = self.driver.find_element(By.XPATH, xpath)
        button.click()

    def click_class_name_button(self, class_name):
        WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.CLASS_NAME, class_name)))
        self.driver.execute_script("document.getElementsByClassName('" + class_name + "')[0].click()")

    def click_on_buttons_by_xpath(self, xpath, button_subtext, location):
        is_found = False
        submit_buttons = self.driver.find_elements(By.XPATH, xpath)
        for button in submit_buttons:
            if button_subtext in button.text:
                is_found = True
                self.driver.execute_script("arguments[0].click()", button)
                break
        if not is_found:
            raise Exception("'" + button_subtext + "' is not found on the " + location + "!")
