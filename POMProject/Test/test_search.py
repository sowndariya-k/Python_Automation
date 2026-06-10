import pytest

from pages.HomePage import HomePage
from pages.SearchPage import SearchPage
from Utilities.logger import get_logger


@pytest.mark.usefixtures("setup_and_teardown")
class TestSearch:

    logger = get_logger()

    @pytest.mark.parametrize("product", ["HP", "Mac", "Samsung"])
    def test_search_for_valid_product(self, product):

        self.logger.info(f"Search Test Started for {product}")

        home_page = HomePage(self.driver)

        home_page.enter_product_into_search_box_field(product)
        self.logger.info(f"Entered Product: {product}")

        home_page.click_search_btn()
        self.logger.info("Clicked Search Button")

        search_page = SearchPage(self.driver)

        assert search_page.display_status_of_valid_product( product)

        self.logger.info(f"Search Test Passed for {product}")