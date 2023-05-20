from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from helpers.elements.ButtonsClick import ButtonsClick


class SignIn:
    driver = None
    buttons_click = None

    def __init__(self, driver):
        self.driver = driver
        self.buttons_click = ButtonsClick(driver)

    def enter_credentials(self, field_id, user_credentials):
        text_field = self.driver.find_element(By.ID, field_id)
        text_field.send_keys(user_credentials)

    def click_on_signin_button(self, button_text):
        self.buttons_click.click_on_button_by_xpath("//input[@value='" + button_text + "']")

    def do_manual_verification(self, website_link):
        WebDriverWait(self.driver, 120).until(
            EC.element_to_be_clickable((By.XPATH,
                                        "//*[@class='Header-item mt-n1 mb-n1  d-none d-md-flex']/a[@href='" +
                                        website_link + "']")))
