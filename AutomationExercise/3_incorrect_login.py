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
home=driver.find_element(By.XPATH,"//div[@class='item active']//h1")
print("Visible home page:", home.is_displayed())

# 3. Click Signup/Login
driver.find_element(By.XPATH,"//a[text()=' Signup / Login']").click()

# 4. Verify Login to your account
login_text=driver.find_element(By.XPATH,"//h2[text()='Login to your account']")
print("Login to your account visible:", login_text.is_displayed())

# 5. Enter correct email and password
driver.find_element(By.XPATH,"//input[@data-qa='login-email']").send_keys("sowndariya12@gmail.com")
driver.find_element(By.XPATH,"//input[@data-qa='login-password']").send_keys("Sow@911!")

# 6. Click Login button
login_btn = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, "//button[text()='Login']"))
)
login_btn.click()
print("Login button click")

#7. verify error message
error=WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located(
        (By.XPATH, "//*[contains(text(),'Your email or password is incorrect!')]")
    )
)
print("Error message visible:", error.is_displayed())
print(error.text)
driver.quit()