import pytest

from pages.HomePage import HomePage
from pages.SearchPage import SearchPage
from pages.ProductPage import ProductPage
from Utilities.logger import get_logger

@pytest.mark.usefixtures("setup_and_teardown")
class TestProduct:
    logger = get_logger()
    def test_display_product_details(self):
        self.logger.info("Product Test Started")
        home_page = HomePage(self.driver)

        home_page.enter_product_into_search_box_field("HP")
        home_page.click_search_btn()

        search_page = SearchPage(self.driver)
        search_page.click_valid_product()

        product_page = ProductPage(self.driver)

        assert product_page.display_status_of_product()
        self.logger.info("Product Test Passed")