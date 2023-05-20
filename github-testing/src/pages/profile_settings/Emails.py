from selenium.webdriver.common.by import By


class Emails:
    driver = None

    def __init__(self, driver):
        self.driver = driver

    def get_account_email(self, user_email):
        actual_email = self.driver.find_element(By.XPATH, "//*[@title='" + user_email + "']")
        return actual_email.text

    def get_account_name(self):
        user_name = self.driver.find_element(By.XPATH, "//main/*/*/*/*")
        return user_name.get_attribute("alt")[1:]
