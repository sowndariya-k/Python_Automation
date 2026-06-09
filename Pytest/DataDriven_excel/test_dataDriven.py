import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from Utitlities import excelReader
from Utitlities import logCreator
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


@pytest.mark.parametrize(
    "username,password",
    excelReader.get_data("ExcelFiles/loginData.xlsx", "login")
)
class TestLogin1:

    logger = logCreator.log_generator()

    def test_validLogin(self, username, password):

        self.logger.info(f"Starting test case with username: {username}")

        driver = webdriver.Chrome()
        driver.maximize_window()

        try:
            self.logger.info("Opening Demoblaze site")
            driver.get("https://demoblaze.com/")

            wait = WebDriverWait(driver, 10)

            self.logger.info("Clicking login button")
            wait.until(EC.element_to_be_clickable((By.ID, "login2"))).click()

            self.logger.info("Entering credentials")
            wait.until(EC.visibility_of_element_located((By.ID, "loginusername"))).send_keys(username)
            wait.until(EC.visibility_of_element_located((By.ID, "loginpassword"))).send_keys(password)

            self.logger.info("Submitting login form")
            wait.until(EC.element_to_be_clickable((By.XPATH, "//button[text()='Log in']"))).click()

            try:
                alert = WebDriverWait(driver, 3).until(EC.alert_is_present())
                text = alert.text
                alert.accept()

                self.logger.warning(f"Login failed for {username}: {text}")

                assert text in ["User does not exist.", "Wrong password."]
                return

            except TimeoutException:
                self.logger.info("No alert detected, login assumed successful")

            logout_btn = wait.until(EC.visibility_of_element_located((By.ID, "logout2")))
            assert logout_btn.is_displayed()

            self.logger.info(f"Login successful for user: {username}")

        finally:
            self.logger.info("Closing browser")
            driver.quit()