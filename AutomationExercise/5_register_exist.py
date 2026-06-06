import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
driver=webdriver.Chrome()
driver.maximize_window()
driver.get("https://automationexercise.com/")
print(driver.title)
home=driver.find_element(By.XPATH,"//div[@class='item active']//h1[1]")
print("Visible home page:", home.is_displayed())
signin=driver.find_element(By.XPATH,"//a[text()=' Signup / Login']").click()
newsign=driver.find_element(By.XPATH,"//h2[text()='New User Signup!']")
print("new user sign up visible :", newsign.is_displayed())

name=driver.find_element(By.XPATH, "//input[@placeholder='Name']")
name.send_keys("sowndariya")

email=driver.find_element(By.XPATH, "//input[@data-qa='signup-email']")
email.send_keys("sowndariya16@gmail.com")
signup=driver.find_element(By.XPATH,"//button[text()='Signup']").click()
print("signup clicked")
#7. verify error message
error=WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located(
        (By.XPATH, "//p[text()='Email Address already exist!']")
    )
)
print("Error message visible:", error.is_displayed())
print(error.text)
driver.quit()