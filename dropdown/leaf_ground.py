import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import Select, WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.leafground.com/select.xhtml")
wait=WebDriverWait(driver, 10)
print(driver.title)
tool=Select(wait.until(EC.presence_of_element_located((By.XPATH,"//select[@class='ui-selectonemenu']"))))
tool.select_by_visible_text("Selenium")

print("Selected Tool:", tool.first_selected_option.text)
time.sleep(2)

country =wait.until(EC.element_to_be_clickable((By.ID, "j_idt87:country_label")))
country.click()
driver.find_element(By.XPATH, "//li[@data-label='India']").click()
print("Country Selected : India")
time.sleep(2)

city= driver.find_element(By.ID,"j_idt87:city_label")
city.click()
driver.find_element(By.ID,"j_idt87:city_2").click()
print("City Selected : Chennai")
time.sleep(2)

course = driver.find_element(By.XPATH, "//input[@placeholder='Choose Course']")
course.send_keys("AWS")
time.sleep(2)
driver.find_element(By.XPATH,"//li[contains(@class,'ui-autocomplete-item')]").click()
print("Course Selected: AWS")

language =driver.find_element(By.ID,"j_idt87:lang_label")
language.click()
driver.find_element(By.ID,"j_idt87:lang_1").click()
print("language Selected : English")
time.sleep(2)

lang_choose=driver.find_element(By.ID,"j_idt87:value_label")
lang_choose.click()
driver.find_element(By.ID,"j_idt87:value_1").click()
print("language choose Selected : One")
time.sleep(2)
driver.quit()