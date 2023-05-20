from selenium.webdriver.common.by import By

from helpers.elements.ButtonsClick import ButtonsClick


class Creation:
    driver = None
    buttons_click = None

    def __init__(self, driver):
        self.driver = driver
        self.buttons_click = ButtonsClick(driver)

    def manage_visibility_option(self, option, to_check):
        visibility = self.driver.find_element(By.XPATH, "//input[@type='radio' and @value='" + option + "']")
        if not to_check:
            visibility.click()
            return None
        else:
            return visibility.get_attribute("checked")

    def fill_fields_with_data(self, text, field_id):
        text_input = self.driver.find_element(By.ID, field_id)
        text_input.send_keys(text)

    def click_on_create_button(self, button_subtext):
        self.buttons_click.click_on_buttons_by_xpath("//button[@type='submit']", button_subtext, "repository settings "
                                                                                                 "creation")
