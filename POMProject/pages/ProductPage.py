from selenium.webdriver.common.by import By

class ProductPage:

    product_name_xpath = "//h1[text()='HP LP3065']"

    def __init__(self, driver):
        self.driver = driver

    def display_status_of_product(self):
        return self.driver.find_element(
            By.XPATH,
            self.product_name_xpath
        ).is_displayed()