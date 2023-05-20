import selenium.common
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from helpers.elements.ButtonsClick import ButtonsClick
from helpers.elements.InputTexts import InputTexts


class General:
    driver = None
    buttons_click = None

    def __init__(self, driver):
        self.driver = driver
        self.buttons_click = ButtonsClick(driver)

    def get_repository_name(self, repository_name):
        hyperlinked_text = WebDriverWait(self.driver, 30).until(
            EC.visibility_of_element_located((By.LINK_TEXT, repository_name)))
        return hyperlinked_text.text

    def click_on_settings(self, settings_id):
        WebDriverWait(self.driver, 15).until(
            EC.element_to_be_clickable((By.ID, settings_id)))
        self.buttons_click.click_on_button_by_id(settings_id)

    def click_on_repository_config(self, button_subtext, element_xpath):
        WebDriverWait(self.driver, 15).until(
            EC.visibility_of_element_located((By.XPATH, "//label[@for='rename-field']")))
        self.buttons_click.click_on_buttons_by_xpath(element_xpath, button_subtext,
                                                     'repository settings alteration')

    def click_on_dropdown_option(self, xpath):
        WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, xpath)))
        # button.click()
        self.buttons_click.click_on_button_by_xpath(xpath)

    def click_on_confirmation_button(self, new_value):
        confirmation_button = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//button[@data-new-visibility='" + new_value + "']")))
        confirmation_button.click()

    def click_on_delete_confirmation(self, action_hyperlink):
        confirmation_button = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//form[@action='" + action_hyperlink + "/settings/delete']/button")))
        confirmation_button.click()

    def get_visibility_value(self, confirmation_value):
        visibility_text = WebDriverWait(self.driver, 30).until(
            EC.visibility_of_element_located((By.XPATH, "//strong/../div")))
        if confirmation_value in visibility_text.text:
            return confirmation_value
        else:
            return None

    def click_on_repository_star(self, star_action, location):
        is_found = False
        submit_buttons = self.driver.find_elements(By.XPATH, "//button[@type='submit']")
        for button in submit_buttons:
            attribute_value = button.get_attribute("aria-label")
            if attribute_value is not None and star_action in attribute_value:
                button.click()
                is_found = True
                break
        if not is_found:
            raise Exception("'" + star_action + "' is not found on the " + location + "!")

    def check_repository_star(self):
        try:
            starred_value = self.driver.execute_script("return this.document.getElementsByClassName('d-flex on')["
                                                       "0].innerText")
            return starred_value
        except selenium.common.exceptions.JavascriptException:
            return False

    def get_confirmation_term(self, repository_name):
        WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.XPATH, "//p/strong")))
        bold_texts = self.driver.find_elements(By.XPATH, "//p/strong")
        for bold_text in bold_texts:
            if repository_name in bold_text.text:
                return bold_text.text
        return None

    def write_on_text_box(self, value):
        xpath = "//*/input[@*='delete']/../*/input[@type='text' and @*='verify']"
        input_texts = InputTexts(self.driver)
        WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.XPATH, xpath)))
        input_texts.add_input_text(xpath, value)
