import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.maximize_window()

# 1. Navigate to URL
driver.get("https://automationexercise.com/")

# 2. Verify Home Page
print(driver.title)
home=driver.find_element(By.XPATH, "//div[@class='item active']//h1")
print("Visible home page:", home.is_displayed())

# 3. Click testcase
driver.find_element(By.XPATH, "//div[@class='item active']//button[@type='button'][normalize-space()='Test Cases']").click()
print("Testcase btn clicked")
print("Current URL:", driver.current_url)

if "test_cases" in driver.current_url:
    print("User navigated to Test Cases page successfully")
driver.quit()