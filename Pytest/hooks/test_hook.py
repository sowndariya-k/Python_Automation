import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

def setup_function(function):
    global driver
    driver=webdriver.Chrome()
    driver.maximize_window()
    driver.implicitly_wait(5)
    driver.get("https://tutorialsninja.com/demo/")

def teardown_function(function):
    driver.quit()

def test_validproduct():
    driver.find_element(By.NAME, "search").send_keys("HP")
    driver.find_element( By.XPATH,"//button[contains(@class,'btn-default')]").click()
    assert driver.find_element(By.LINK_TEXT,"HP LP3065").is_displayed()
