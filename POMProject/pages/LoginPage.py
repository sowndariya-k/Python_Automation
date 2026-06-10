from selenium.webdriver.common.by import By

class LoginPage:

    email_field_id = "input-email"
    password_field_id = "input-password"
    login_button_xpath = "//input[@value='Login']"
    my_account_heading_xpath = "//h2[text()='My Account']"

    def __init__(self, driver):
        self.driver = driver

    def enter_email(self, email):
        self.driver.find_element(By.ID, self.email_field_id).send_keys(email)

    def enter_password(self, password):
        self.driver.find_element(By.ID, self.password_field_id).send_keys(password)

    def click_login_button(self):
        self.driver.find_element(By.XPATH, self.login_button_xpath).click()

    def display_status_of_login(self):
        return self.driver.find_element(
            By.XPATH,
            self.my_account_heading_xpath
        ).is_displayed()