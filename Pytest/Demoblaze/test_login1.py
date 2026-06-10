import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import read_config

@pytest.mark.usefixtures("setup_and_teardown")
class TestLogin:

    def test_validlogin(self):
        login_link = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.ID, "login2")))
        login_link.click()
        username = read_config.get_config("login credential", "username")
        password = read_config.get_config("login credential", "password")
        self.driver.find_element(By.ID, "loginusername").send_keys(username)
        self.driver.find_element(By.ID, "loginpassword").send_keys(password)
        loginbtn=WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[text()='Log in']")))
        loginbtn.click()
        logout_btn = WebDriverWait(self.driver, 15).until(EC.visibility_of_element_located((By.ID, "logout2")))
        assert logout_btn.is_displayed()

    def test_invalidlogin(self):
        self.driver.find_element(By.ID, "login2").click()
        username = read_config.get_config("Invalid password", "username")
        password = read_config.get_config("Invalid password", "password")
        self.driver.find_element(By.ID, "loginusername").send_keys(username)
        self.driver.find_element(By.ID, "loginpassword").send_keys(password)
        self.driver.find_element(By.XPATH, "//button[text()='Log in']").click()
        alert = WebDriverWait(self.driver, 10).until(EC.alert_is_present())
        assert alert.text == "Wrong password."
        alert.accept()

    def test_invalidloginuser(self):
            self.driver.find_element(By.ID, "login2").click()
            username = read_config.get_config("Invalid user", "username")
            password = read_config.get_config("Invalid user", "password")
            self.driver.find_element(By.ID, "loginusername").send_keys(username)
            self.driver.find_element(By.ID, "loginpassword").send_keys(password)
            self.driver.find_element(By.XPATH, "//button[text()='Log in']").click()
            alert = WebDriverWait(self.driver, 10).until(EC.alert_is_present())
            assert alert.text == "User does not exist."
            alert.accept()