import time
from selenium import webdriver
from selenium.webdriver.common.by import By
driver=webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.google.com/")
print(driver.title)

search_box=driver.find_element(By.NAME,"q")
print("Enabled:", search_box.is_enabled())
if search_box. is_enabled():
    search_box.send_keys("Selenium python")
else:
    print("Search box not found")
time.sleep(2)

search = driver.find_element(By.NAME, "btnK")
print("Search Button:", search.is_enabled())
if search.is_enabled():
    search.click()
else:
    print("not enable search")
time.sleep(5)
driver.quit()
