from selenium.webdriver.common.by import By

from helpers.data_processing import Constants
from utils.ManageFiles import ManageFiles
from helpers.elements.InputTexts import InputTexts


class SearchResults:
    driver = None
    input_texts = None
    manage_files = None

    def __init__(self, driver):
        self.driver = driver
        self.input_texts = InputTexts(driver)
        self.manage_files = ManageFiles()

    def search_for_term(self, search_term):
        self.input_texts.set_input_value("//input[@type='text' and @name='q']", search_term)

    def hit_search(self):
        self.input_texts.add_input_text("//input[@type='text' and @name='q']", "\n")

    def check_search_completion(self, search_term):
        self.input_texts.get_texts_by_xpath("//h3", search_term)

    def star_valid_results(self, search_term, test_case_id):
        python_repo_count = 0
        file_name = Constants.OUTPUT_FILE_NAME + "-" + test_case_id
        self.manage_files.open_writer_csv(file_name, ["Repository Name", "Project Name", "Stars Count"])
        search_term_length = len(search_term)
        headlines = self.driver.find_elements(By.PARTIAL_LINK_TEXT, search_term)
        headlines.extend(self.driver.find_elements(By.PARTIAL_LINK_TEXT, search_term.upper()))
        headlines.extend(self.driver.find_elements(By.PARTIAL_LINK_TEXT, search_term.lower()))
        unique_headlines = list(dict.fromkeys(headlines))
        result_position = 0
        for headline in unique_headlines:
            index = headline.text.find("/")
            if index >= 0:
                result_position += 1
                sub_headline = headline.text[index + 1::1]
                if len(sub_headline) == search_term_length:
                    project_name = headline.text[0:index:1]
                    stars_count = self.driver.find_element(By.XPATH, "//ul[@class='repo-list']/li[" +
                                                           str(result_position) + "]/div[2]/*[3]/*/*/a")
                    self.manage_files.write_to_csv([headline.text, project_name, stars_count.text])
                    python_repo_count += 1
        return python_repo_count

    def read_search_results_file(self, test_case_id):
        file_name = Constants.OUTPUT_FILE_NAME + "-" + test_case_id
        stars_list = self.manage_files.read_from_csv(file_name, "list")
        return len(stars_list)

    def get_stars_list(self, test_case_id):
        file_name = Constants.OUTPUT_FILE_NAME + "-" + test_case_id
        stars_list = self.manage_files.read_from_csv(file_name, "list")
        return stars_list
