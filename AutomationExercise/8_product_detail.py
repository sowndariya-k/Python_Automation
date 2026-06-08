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

driver.find_element(By.XPATH,"//a[@href='/products']").click()
print("product btn clicked")
print("Current URL:", driver.current_url)
if "products" in driver.current_url:
    print("User navigated to all product page successfully")

products=driver.find_element(By.XPATH, "//div[@class='features_items']")
print("Visible all product list:", products.is_displayed())

# 6. Click on first View Product button using JavaScript
view_product = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located(
        (By.XPATH, "(//a[contains(text(),'View Product')])[1]")
    )
)

driver.execute_script("arguments[0].scrollIntoView(true);", view_product)
time.sleep(2)
view_product = driver.find_element(By.XPATH,"(//a[contains(text(),'View Product')])[1]")
driver.execute_script("arguments[0].click();", view_product)

# 7. Verify user is landed on product detail page
WebDriverWait(driver, 10).until(EC.url_contains("product_details"))
print("View Product clicked")
print("Current URL:", driver.current_url)
if "product_details" in driver.current_url:
    print("User entered product detail page successfully")
time.sleep(3)
driver.quit()