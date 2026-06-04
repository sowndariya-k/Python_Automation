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
email.send_keys("sowndariya911@gmail.com")
signup=driver.find_element(By.XPATH,"//button[text()='Signup']").click()
print("signup clicked")

name_new=driver.find_element(By.ID, "name")
email_new=driver.find_element(By.ID, "email")
print(name_new.get_attribute("value"))
print(email_new.get_attribute("value"))

account_info = driver.find_element(By.XPATH,"//b[text()='Enter Account Information']")
print("ENTER ACCOUNT INFORMATION visible:",account_info.is_displayed())

title=driver.find_element(By.XPATH, "//input[@id='id_gender2']")
title.click()
password=driver.find_element(By.ID,"password")
password.send_keys("Sow@911!")
day = Select(driver.find_element(By.ID, "days"))
day.select_by_visible_text("9")
month=Select(driver.find_element(By.ID, "months"))
month.select_by_visible_text("November")
year=Select(driver.find_element(By.ID, "years"))
year.select_by_visible_text("2000")

checkbox=driver.find_element(By.NAME,"newsletter").click()
checkbox2=driver.find_element(By.NAME,"optin").click()

firstname=driver.find_element(By.NAME,"first_name")
firstname.send_keys("Sowndariya")
lastname=driver.find_element(By.NAME,"last_name")
lastname.send_keys("K")
company=driver.find_element(By.NAME,"company")
company.send_keys("KIOT")
driver.find_element(By.ID, "address1").send_keys("Salem")
driver.find_element(By.ID, "address2").send_keys("Tamil Nadu")

Select(driver.find_element(By.ID, "country")).select_by_visible_text("India")

driver.find_element(By.ID, "state").send_keys("Tamil Nadu")
driver.find_element(By.ID, "city").send_keys("Salem")
driver.find_element(By.ID, "zipcode").send_keys("636005")
driver.find_element(By.ID, "mobile_number").send_keys("9876543210")

# 11. Create Account
driver.find_element(By.XPATH, "//button[text()='Create Account']").click()

# 12. Verify Account Created
account_created = driver.find_element(By.XPATH, "//b[text()='Account Created!']")
print("ACCOUNT CREATED:", account_created.is_displayed())

# 13. Continue
driver.find_element(By.XPATH, "//a[text()='Continue']").click()

# 14. Verify Logged In
logged_in = driver.find_element(By.XPATH, "//a[contains(text(),'Logged in as')]")
print("Logged In:", logged_in.is_displayed())
print(logged_in.text)

# Delete Account
delete_btn = driver.find_element(By.XPATH,"//a[contains(text(),'Delete Account')]")
print("Delete button visible:", delete_btn.is_displayed())
print("Delete button enabled:", delete_btn.is_enabled())
#javascript executor
driver.execute_script("arguments[0].click();", delete_btn)
time.sleep(5)
print("Current URL =", driver.current_url)
print("Page Title =", driver.title)

# Verify Account Deleted
account_deleted = WebDriverWait(driver, 15).until(
    EC.visibility_of_element_located((By.XPATH, "//*[contains(text(),'Account Deleted')]")))
print("ACCOUNT DELETED:", account_deleted.is_displayed())

# 17. Continue
driver.find_element(By.XPATH, "//a[text()='Continue']").click()
time.sleep(3)
driver.close()