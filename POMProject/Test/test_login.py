import pytest

from pages.HomePage import HomePage
from pages.LoginPage import LoginPage
from Utilities.read_config import ReadConfig
from Utilities.logger import get_logger

@pytest.mark.usefixtures("setup_and_teardown")
class TestLogin:
    logger = get_logger()
    def test_login_with_valid_credentials(self):
        self.logger.info("login test start")
        home_page = HomePage(self.driver)

        home_page.click_my_account()
        home_page.select_login_option()

        login_page = LoginPage(self.driver)

        login_page.enter_email(
            ReadConfig.get_email()
        )

        login_page.enter_password(
            ReadConfig.get_password()
        )

        login_page.click_login_button()

        assert login_page.display_status_of_login()
        self.logger.info("valid login verified")