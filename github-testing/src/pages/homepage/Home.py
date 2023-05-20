from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

from helpers.elements.ButtonsClick import ButtonsClick
from pages.repository.Creation import Creation


class Home:
    driver = None
    buttons_click = None
    repository_creation = None

    def __init__(self, driver):
        self.driver = driver
        self.buttons_click = ButtonsClick(driver)
        self.repository_creation = Creation(driver)

    def click_on_profile(self, class_name):
        self.buttons_click.click_class_name_button(class_name)
        WebDriverWait(self.driver, 20).until(
            EC.visibility_of_element_located((By.PARTIAL_LINK_TEXT, "Signed in as")))

    def select_from_dropdown_list(self, selection_name):
        self.buttons_click.click_hyperlinked_buttons(selection_name)

    def click_on_website_icon(self, website_link):
        website_icon = self.driver.find_element(By.XPATH,
                                                "//*[@class='Header-item mt-n1 mb-n1  d-none d-md-flex']/a[@href='" +
                                                website_link + "']")
        website_icon.click()

    def click_on_action_button(self, button_text):
        self.buttons_click.click_hyperlinked_buttons(button_text)

    def scroll_to_the_top(self):
        body = self.driver.find_element(By.XPATH, "//body")
        body.send_keys(Keys.CONTROL + Keys.HOME)
