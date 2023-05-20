import selenium.common.exceptions
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from helpers.elements.ButtonsClick import ButtonsClick


class GuestView:
    driver = None
    buttons_click = None

    def __init__(self, driver):
        self.driver = driver
        self.buttons_click = ButtonsClick(driver)

    def click_on_header_menu(self, button_substring):
        self.buttons_click.click_hyperlinked_buttons(button_substring)

    def check_sign_in_button(self, button_substring):
        try:
            WebDriverWait(self.driver, 20).until(
                EC.element_to_be_clickable((By.PARTIAL_LINK_TEXT, button_substring)))
            return True
        except selenium.common.exceptions.TimeoutException:
            return False
