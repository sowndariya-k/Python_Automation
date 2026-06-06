import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os
driver=webdriver.Chrome()
driver.maximize_window()
driver.get("https://automationexercise.com/")
print(driver.title)
home=driver.find_element(By.XPATH,"//div[@class='item active']//h1[1]")
print("Visible home page:", home.is_displayed())
contact=driver.find_element(By.XPATH,"//a[normalize-space()='Contact us']").click()
get_touch=driver.find_element(By.XPATH, "//h2[text()='Get In Touch']")
print("Get in touch is visible :", get_touch.is_displayed())

name=driver.find_element(By.XPATH, "//input[@placeholder='Name']")
name.send_keys("sowndariya")

email=driver.find_element(By.XPATH, "//input[@placeholder='Email']")
email.send_keys("sowndariya16@gmail.com")

subject=driver.find_element(By.XPATH, "//input[@placeholder='Subject']")
subject.send_keys("Request demo website testing use")

message=driver.find_element(By.XPATH, "//textarea[@placeholder='Your Message Here']")
message.send_keys("use the autoexercise for testing learning")

file_path = os.path.abspath("upload.txt")
upload=driver.find_element(By.XPATH,"//input[@name='upload_file']")
upload.send_keys(file_path)
print("upload file clicked")

submit=driver.find_element(By.XPATH,"//input[@name='submit']").click()
print("submit btn clicked")
#accept alert
WebDriverWait(driver, 5).until(EC.alert_is_present())
driver.switch_to.alert.accept()
print("Alert OK clicked")
success=driver.find_element(By.XPATH, "//div[@class='status alert alert-success']")
print("success message is visible :", success.is_displayed())

driver.find_element(By.XPATH,"//span[normalize-space()='Home']").click()
home=WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.XPATH,"//div[@class='item active']//h1[1]"))
)
print("Visible home page:", home.is_displayed())
driver.quit()