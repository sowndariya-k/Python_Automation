import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://omayo.blogspot.com/")

# Text Area
textarea = driver.find_element(By.ID, "ta1")

# send_keys()
textarea.send_keys("Hello Selenium")
time.sleep(2)

# get_attribute()
print("Attribute:", textarea.get_attribute("id"))

# tag_name
print("Tag Name:", textarea.tag_name)

# location
print("Location:", textarea.location)

# size
print("Size:", textarea.size)

# value_of_css_property()
print("Font:", textarea.value_of_css_property("font-family"))

# clear()
textarea.clear()
time.sleep(2)

# send_keys again
textarea.send_keys("Testing Commands")

# is_displayed()
print("Displayed:", textarea.is_displayed())

# is_enabled()
print("Enabled:", textarea.is_enabled())

# Checkbox
checkbox = driver.find_element(By.ID, "checkbox1")

# click()
checkbox.click()
time.sleep(2)

# is_selected()
print("Selected:", checkbox.is_selected())

# Button
button = driver.find_element(By.ID, "but1")

# text
print("Button Text:", button.text)

# Save Screenshot
driver.save_screenshot("omayo.png")

# Submit (using form element)
search_box = driver.find_element(By.NAME, "q")
search_box.send_keys("Selenium")
search_box.submit()

time.sleep(3)

driver.back()

# Page text
print("Page Title:", driver.title)

driver.quit()