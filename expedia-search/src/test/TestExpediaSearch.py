from unittest import TestCase
from core.ManageCsv import ManageCsv
from core.OpenBrowser import OpenBrowser
from pages.BingSearchBox import BingSearchBox
from pages.BingSearchResults import BingSearchResults
from ddt import ddt, data, unpack


@ddt
class TestExpediaSearch(TestCase):
    driver = None
    bing_box = None
    manage_csv = ManageCsv()

    @classmethod
    def setUpClass(cls):
        browser = OpenBrowser("chrome")
        cls.driver = browser.create_driver(True)
        cls.bing_box = BingSearchBox(cls.driver)
        cls.manage_csv.open_writer_csv("search-results.csv")

    @data(*manage_csv.read_from_csv("input-file.csv"))
    @unpack
    def testGetRequests(self, hotel_name, city, address):
        not_found_count = 0

        self.driver.get("https://www.bing.com")
        self.bing_box.search_term(hotel_name, city)
        self.bing_box.submit_search()

        self.bing_results = BingSearchResults(self.driver)
        self.bing_results.get_search_results()

        page_results_count = self.bing_results.get_results_count()

        search_status = self.bing_results.check_next_search_result()
        while search_status != -1:
            match search_status:
                case 1:
                    self.manage_csv.write_to_csv([hotel_name, address, self.bing_results.get_website_link()])
                case 0:
                    not_found_count += 1
                case _:
                    raise RuntimeError("Unknown search result!")
            search_status = self.bing_results.check_next_search_result()

        if not_found_count >= page_results_count:
            self.manage_csv.write_to_csv(["Hotel not found!", address, ""])

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()
