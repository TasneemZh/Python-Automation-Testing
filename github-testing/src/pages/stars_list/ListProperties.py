from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from helpers.elements.ButtonsClick import ButtonsClick
from helpers.elements.InputTexts import InputTexts


class ListProperties:
    driver = None
    input_texts = None
    buttons_click = None

    def __init__(self, driver):
        self.driver = driver
        self.input_texts = InputTexts(driver)
        self.buttons_click = ButtonsClick(driver)

    def fill_list_name(self, list_name):
        self.input_texts.set_input_value("//input[@name='user_list[name]']", list_name)

    def fill_list_description(self, list_description):
        self.input_texts.add_input_text("//textarea[@name='user_list[description]']", list_description)

    def check_creation_completion(self):
        WebDriverWait(self.driver, 20).until(
            EC.visibility_of_element_located((By.ID, "user-profile-frame")))

    def get_list_name(self):
        return self.input_texts.get_text_by_xpath("//turbo-frame[@id='user-profile-frame']/*/div/div[1]/*")

    def check_action_completion(self, popup_headline):
        WebDriverWait(self.driver, 20).until(
            EC.invisibility_of_element_located((By.XPATH, "//details-dialog[@aria-label='" + popup_headline + "']")))

    def close_informative_message(self):
        WebDriverWait(self.driver, 20).until(
            EC.visibility_of_element_located((By.XPATH, "//div[@role='alert']")))
        self.buttons_click.click_on_button_by_xpath("//button[@aria-label='Dismiss this message']")

    def click_on_user_list(self, user_name, list_name):
        self.buttons_click.click_on_button_by_xpath("//a[@href='/stars/" + user_name + "/lists/"
                                                    + list_name.replace(" ", "-").lower() + "']")

    def click_on_edit_list(self):
        WebDriverWait(self.driver, 30).until(
            EC.presence_of_element_located((By.PARTIAL_LINK_TEXT, "Explore repositories")))
        self.buttons_click.click_on_buttons_by_xpath("//summary[@role='button']", "Edit list", "Lists Properties")

    def confirm_deletion(self):
        self.buttons_click.click_on_buttons_by_xpath("//button[@type='submit']", "Delete", "Lists Properties")

    def go_back_to_lists(self, xpath):
        hyperlink = WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located((By.XPATH, xpath)))
        hyperlink.click()
