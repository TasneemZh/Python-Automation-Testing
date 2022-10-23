from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By


class BingSearchResults:
    driver = None
    results_list = []
    index = 0
    website_link = None

    def __init__(self, driver):
        self.driver = driver

    def get_search_results(self):
        self.results_list = self.driver.find_elements(By.XPATH, '//*[@id="b_results"]/li')

    def check_next_search_result(self):
        print("\nSearch Results Length: " + str(len(self.results_list)))
        if self.index == len(self.results_list):
            return -1
        print("\nIndex in Search Results: " + str(self.index))
        self.index += 1
        try:
            result = self.driver.find_element(By.XPATH, '//*[@id="b_results"]/li[' + str(self.index) + ']/h2/a')
        except NoSuchElementException:
            print("Oops! There's an error...")
            return 0
        self.website_link = result.get_attribute('href')
        # try:
        #     print("\nWebsite Link: " + self.website_link)
        # except TypeError:
        #     None
        if self.website_link is not None:
            if self.website_link.find('expedia.com') != -1 & self.website_link.endswith('Hotel-Information'):
                return 1
        return 0

    def get_website_link(self):
        return self.website_link

    def get_results_count(self):
        return len(self.results_list)
