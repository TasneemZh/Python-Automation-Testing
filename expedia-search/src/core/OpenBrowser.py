from selenium import webdriver
from selenium.webdriver.chrome.options import Options


class OpenBrowser:
    browser = None

    def __init__(self, browser):
        self.browser = browser

    def create_driver(self, isHeadless):
        match self.browser:
            case "chrome":
                options = Options()
                options.headless = isHeadless
                driver = webdriver.Chrome("../../resources/drivers/chromedriver", options=options)
            case "edge":
                driver = webdriver.Edge("../../resources/drivers/msedgedriver")
            case "firefox":
                driver = webdriver.Firefox("../../resources/drivers/geckodriver")
            case _:
                raise RuntimeError("Unsupported browser!")
        driver.implicitly_wait(5)
        driver.maximize_window()
        return driver
