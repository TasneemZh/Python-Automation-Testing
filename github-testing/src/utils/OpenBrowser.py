from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from msedge.selenium_tools import EdgeOptions, Edge
from selenium import webdriver

from utils.ManageFiles import ManageFiles


class OpenBrowser:
    @staticmethod
    def create_driver():
        manage_files = ManageFiles()
        config = manage_files.read_from_json("config")
        if config["browser"] == "chrome":
            options = webdriver.ChromeOptions()
            if config["headless_mode"]:
                options.add_argument("--headless")
            driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
        elif config["browser"] == "firefox":
            options = webdriver.FirefoxOptions()
            if config["headless_mode"]:
                options.headless = True
            driver = webdriver.Firefox(executable_path=GeckoDriverManager().install(), options=options)
        elif config["browser"] == "edge":
            options = EdgeOptions()
            options.use_chromium = True
            if config["headless_mode"]:
                options.headless = True
            driver = Edge(executable_path=EdgeChromiumDriverManager().install(), options=options)
        else:
            raise Exception("Unsupported browser!")
        driver.implicitly_wait(config["timeout"])
        driver.maximize_window()
        return driver
