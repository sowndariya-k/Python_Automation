import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import read_config


@pytest.mark.usefixtures("setup_and_teardown")
class TestLogin:

    def test_validLogin(self):

        wait = WebDriverWait(self.driver, 20)

        # click login button safely
        login_btn = wait.until(EC.element_to_be_clickable((By.ID, "login2")))
        login_btn.click()

        wait.until(EC.visibility_of_element_located((By.ID, "loginusername"))).send_keys(
            read_config.get_config("login credential", "username")
        )

        wait.until(EC.visibility_of_element_located((By.ID, "loginpassword"))).send_keys(
            read_config.get_config("login credential", "password")
        )

        wait.until(EC.element_to_be_clickable((By.XPATH, "//button[text()='Log in']"))).click()

        assert wait.until(
            EC.visibility_of_element_located((By.ID, "logout2"))
        ).is_displayed()


    def test_invaliduser(self):

        wait = WebDriverWait(self.driver, 20)

        wait.until(EC.element_to_be_clickable((By.ID, "login2"))).click()

        wait.until(EC.visibility_of_element_located((By.ID, "loginusername"))).send_keys(
            read_config.get_config("Invalid user", "username")
        )

        wait.until(EC.visibility_of_element_located((By.ID, "loginpassword"))).send_keys(
            read_config.get_config("Invalid user", "password")
        )

        wait.until(EC.element_to_be_clickable((By.XPATH, "//button[text()='Log in']"))).click()

        # Demoblaze shows modal text, not real alert sometimes
        error = wait.until(
            EC.visibility_of_element_located((By.XPATH, "//div[@class='modal-content']"))
        )

        assert "User does not exist" in error.text or "Wrong password" in error.text


    def test_invalidpassword(self):

        wait = WebDriverWait(self.driver, 20)

        wait.until(EC.element_to_be_clickable((By.ID, "login2"))).click()

        wait.until(EC.visibility_of_element_located((By.ID, "loginusername"))).send_keys(
            read_config.get_config("Invalid password", "username")
        )

        wait.until(EC.visibility_of_element_located((By.ID, "loginpassword"))).send_keys(
            read_config.get_config("Invalid password", "password")
        )

        wait.until(EC.element_to_be_clickable((By.XPATH, "//button[text()='Log in']"))).click()

        error = wait.until(
            EC.visibility_of_element_located((By.XPATH, "//div[@class='modal-content']"))
        )

        assert "Wrong password" in error.text or "User does not exist" in error.text