from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.actions.wheel_input import ScrollOrigin
import time

driver=webdriver.Chrome()
driver.maximize_window()
driver.get("https://testautomationpractice.blogspot.com/")
actions=ActionChains(driver)

# 3. scroll_from_origin()
print("Scrolling from origin")
table=driver.find_element(By.ID, "productTable")
origin=ScrollOrigin.from_element(table)
actions.scroll_from_origin(origin, 0, 300).perform()
time.sleep(2)
print("All scrolling actions completed.")
driver.quit()