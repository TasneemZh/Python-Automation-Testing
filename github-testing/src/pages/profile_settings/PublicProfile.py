import os

import selenium.common.exceptions
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from utils.ManageFiles import ManageFiles


class PublicProfile:
    driver = None
    number_of_tries = 0

    def __init__(self, driver):
        self.driver = driver

    def click_on_account_menu(self, category_name, item_name):
        index = 1
        list_path = "//ul[@aria-label='" + category_name + "']/li"
        WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, list_path + "[1]")))
        list_items = self.driver.find_elements(By.XPATH, list_path)
        while index < len(list_items):
            item = self.driver.find_element(By.XPATH, list_path + "[" + str(index) + "]/*/span[2]")
            if item_name in item.text:
                item.click()
                break
            else:
                index += 1
        if index >= len(list_items):
            raise Exception("'" + item_name + "' is not found on the account menu!")

    def click_on_edit_profile(self, class_name):
        edit_button = self.driver.find_element(By.XPATH, "//img[@class='" + class_name + "']/../div")
        edit_button.click()

    def upload_profile_image(self, file_name, file_extension):
        manage_files = ManageFiles()
        config = manage_files.read_from_json("config")
        if config["run_command"]:
            relative_path = "./"
        else:
            relative_path = "../../"
        upload_input = self.driver.find_element(By.XPATH, "//input[@type='file']")
        if config["run_command"]:
            upload_input.send_keys(os.path.abspath(
                relative_path + "resources/profiles/" + file_name + "." + file_extension))
        else:
            upload_input.send_keys(os.path.abspath(
                relative_path + "resources/profiles/" + file_name + "." + file_extension))

    def submit_image(self):
        submit_button = self.driver.find_element(By.XPATH, "//button[@name='op']")
        self.driver.execute_script("arguments[0].click()", submit_button)

    def accept_alert_if_exist(self):
        if WebDriverWait(self.driver, 15).until(
                EC.alert_is_present()):
            Alert(self.driver).accept()
            return True
        else:
            return False

    def check_action_image_alert(self, alert_message):
        try:
            if self.accept_alert_if_exist():
                self.number_of_tries = self.number_of_tries + 1
                return None
        except selenium.common.exceptions.TimeoutException:
            WebDriverWait(self.driver, 30).until(
                EC.visibility_of_element_located((By.ID, "js-flash-container")))
            if self.driver.find_elements(By.XPATH, "//*[@role='alert']"):
                alert_content = self.driver.find_element(By.XPATH, "//*[@role='alert']")
                if alert_message in alert_content.text:
                    return True
            return False

    def click_on_remove_image(self):
        remove_button = self.driver.find_element(By.XPATH, "//*[@*='submit' and @*='reset']")
        remove_button.click()

    def reset_tries_count(self):
        self.number_of_tries = 0

    def get_tries_count(self):
        return self.number_of_tries
