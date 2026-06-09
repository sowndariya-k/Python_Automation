import pytest
from selenium.webdriver.common.by import By
import read_config

@pytest.mark.usefixtures("setup_and_teardown")
class TestSearch:

    def test_search_valid_product(self):

        self.driver.find_element(
            By.NAME, "search"
        ).send_keys(
            read_config.get_config("search term", "validterm")
        )

        self.driver.find_element(
            By.XPATH,
            "//button[contains(@class,'btn-default')]"
        ).click()

        assert "HP" in self.driver.page_source

    def test_search_invalid_product(self):

        self.driver.find_element(
            By.NAME, "search"
        ).send_keys(
            read_config.get_config("search term", "invalidterm")
        )

        self.driver.find_element(
            By.XPATH,
            "//button[contains(@class,'btn-default')]"
        ).click()

        expected_message = "There is no product that matches the search criteria."

        actual_message = self.driver.find_element(
            By.XPATH,
            "//input[@id='button-search']/following-sibling::p"
        ).text

        assert actual_message == expected_message