from selenium.webdriver.common.by import By

class HomePage:

    my_account_xpath = "//span[text()='My Account']"
    login_link_text = "Login"

    search_box_field_name = "search"
    search_button_xpath = "//button[@class='btn btn-default btn-lg']"

    def __init__(self, driver):
        self.driver = driver

    def click_my_account(self):
        self.driver.find_element(By.XPATH, self.my_account_xpath).click()

    def select_login_option(self):
        self.driver.find_element(By.LINK_TEXT, self.login_link_text).click()

    def enter_product_into_search_box_field(self, product_name):
        self.driver.find_element(By.NAME, self.search_box_field_name).send_keys(product_name)

    def click_search_btn(self):
        self.driver.find_element(By.XPATH, self.search_button_xpath).click()