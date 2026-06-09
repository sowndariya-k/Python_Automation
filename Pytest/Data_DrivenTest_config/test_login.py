import pytest
from selenium.webdriver.common.by import By
import read_config


@pytest.mark.usefixtures("setup_and_teardown")
class TestLogin:

    def test_validLogin(self):

        self.driver.get(read_config.get_config("basic info", "url"))

        self.driver.find_element(By.ID, "login2").click()

        self.driver.find_element(By.ID, "loginusername").send_keys(
            read_config.get_config("login credential", "username")
        )

        self.driver.find_element(By.ID, "loginpassword").send_keys(
            read_config.get_config("login credential", "password")
        )

        self.driver.find_element(By.XPATH, "//button[text()='Log in']").click()

        logout = self.driver.find_element(By.ID, "logout2")
        assert logout.is_displayed()