import pytest
from selenium.webdriver.common.by import By
import read_config


@pytest.mark.usefixtures("setup_and_teardown")
class TestLogin:

    def test_validLogin(self):

        self.driver.find_element(By.XPATH,"//span[text()='My Account']").click()

        self.driver.find_element(By.LINK_TEXT,"Login").click()
        self.driver.find_element(By.ID,"input-email").send_keys(read_config.get_config("login credential","username"))
        self.driver.find_element(By.ID,"input-password").send_keys(read_config.get_config("login credential","password"))
        self.driver.find_element(By.XPATH,"//input[@value='Login']").click()
        assert "account" in self.driver.current_url.lower()