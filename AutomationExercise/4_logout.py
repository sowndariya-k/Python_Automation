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

# 3. Click Signup/Login
driver.find_element(By.XPATH, "//a[text()=' Signup / Login']").click()

# 4. Verify Login to your account
login_text=driver.find_element(By.XPATH, "//h2[text()='Login to your account']")
print("Login to your account visible:", login_text.is_displayed())

# 5. Enter correct email and password
driver.find_element(By.XPATH, "//input[@data-qa='login-email']").send_keys("sowndariya17@gmail.com")
driver.find_element(By.XPATH, "//input[@data-qa='login-password']").send_keys("Sow@911!")

# 6. Click Login button
login_btn = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, "//button[text()='Login']"))
)
login_btn.click()
print("Login button click")

# 7. Verify Logged in as username
logged_in = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located(
        (By.XPATH, "//a[contains(text(),'Logged in as')]")
    )
)
print("Logged In:", logged_in.is_displayed())
print(logged_in.text)

#8. user logout
logout= WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, "//a[text()=' Logout']"))).click()
print("Logout clicked")

#9. navigate to the login page 
login_page = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.XPATH, "//h2[text()='Login to your account']")))
print("Redirected to login page:", login_page.is_displayed())
time.sleep(3)
driver.quit()