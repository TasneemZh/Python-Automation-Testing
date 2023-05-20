import selenium.common.exceptions
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from helpers.elements.ButtonsClick import ButtonsClick


class View:
    driver = None
    buttons_click = None

    def __init__(self, driver):
        self.driver = driver
        self.buttons_click = ButtonsClick(driver)

    def get_stars_number(self):
        WebDriverWait(self.driver, 20).until(
            EC.visibility_of_element_located((By.ID, "user-starred-repos")))
        stars_rows = self.driver.find_elements(By.XPATH, "//turbo-frame[@id='user-starred-repos']/*/*/*")
        if len(stars_rows) == 2:
            try:
                self.driver.find_element(By.XPATH, "//turbo-frame[@id='user-starred-repos']/*/*/*[2]/h3")
                return 0
            except selenium.common.exceptions.NoSuchElementException:
                return len(stars_rows) - 1  # without the Stars header
        else:
            return len(stars_rows) - 1  # without the Stars header

    def click_on_tab(self, tab_name):
        tab_buttons = self.driver.find_elements(By.XPATH, "//a[@data-tab-item='" + tab_name.lower() + "']")
        tab_buttons[0].click()

    def click_on_specific_repository(self, repo_name):
        self.buttons_click.click_hyperlinked_buttons(repo_name)

    def get_lists_number(self):
        lists_count = self.driver.find_element(By.XPATH, "//turbo-frame[@id='user-profile-frame']/*/*/h2/span")
        list_size = lists_count.text.replace('(', '')
        return int(list_size.replace(')', ''))

    def get_repositories_number(self):
        repositories = self.driver.find_elements(By.XPATH, "//*[@id='user-repositories-list']/*/li")
        return len(repositories)

    def star_repository(self, user_name, repo_name, star_action):
        repository_star = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//a[@href='/" + user_name + "/" + repo_name +
                                        "']/../../../../div[2]/*/*/*/button[@aria-label='" +
                                        star_action + "']")))
        repository_star.click()

    def click_on_create_list(self):
        self.buttons_click.click_on_buttons_by_xpath("//summary[@role='button']", "Create list", "Stars and Lists")
