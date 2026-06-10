from selenium.webdriver.common.by import By

class SearchPage:
    valid_product_link_text = "HP LP3065"
    def __init__(self, driver):
        self.driver = driver

    def display_status_of_valid_product(self, product):
        return self.driver.find_element(
            By.PARTIAL_LINK_TEXT,
            product
        ).is_displayed()
    
    def click_valid_product(self):
        self.driver.find_element(
            By.LINK_TEXT,
            self.valid_product_link_text
        ).click()