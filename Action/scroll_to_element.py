from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.actions.wheel_input import ScrollOrigin
import time

driver=webdriver.Chrome()
driver.maximize_window()
driver.get("https://testautomationpractice.blogspot.com/")
actions=ActionChains(driver)

# 2. scroll_to_element()
print("Scrolling to element")
table=driver.find_element(By.ID, "productTable")
actions.scroll_to_element(table).perform()
time.sleep(2)