from selenium.webdriver.common.by import By


class InputTexts:
    driver = None

    def __init__(self, driver):
        self.driver = driver

    def set_input_value(self, xpath, input_data):
        text_input = self.driver.find_element(By.XPATH, xpath)
        self.driver.execute_script("arguments[0].setAttribute('value',arguments[1])", text_input, input_data)

    def add_input_text(self, xpath, input_data):
        text_input = self.driver.find_element(By.XPATH, xpath)
        text_input.send_keys(input_data)

    def get_text_by_xpath(self, xpath):
        element_text = self.driver.find_element(By.XPATH, xpath)
        return element_text.text

    def get_texts_by_xpath(self, xpath, subtext):
        is_found = False
        element_texts = self.driver.find_elements(By.XPATH, xpath)
        for element_text in element_texts:
            if subtext in element_text.text:
                return element_text.text
                break
        if not is_found:
            raise Exception("'" + button_subtext + "' is not found on the " + location + "!")
