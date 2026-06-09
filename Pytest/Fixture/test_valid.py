from selenium.webdriver.common.by import By

def test_validproduct(setup_and_teardown):

    driver = setup_and_teardown

    driver.find_element(By.NAME, "search").send_keys("HP")

    driver.find_element(
        By.XPATH,
        "//button[contains(@class,'btn-default')]"
    ).click()

    assert driver.find_element(
        By.LINK_TEXT,
        "HP LP3065"
    ).is_displayed()


def test_invalidproduct(setup_and_teardown):

    driver = setup_and_teardown

    driver.find_element(By.NAME, "search").send_keys("Honda")

    driver.find_element(
        By.XPATH,
        "//button[contains(@class,'btn-default')]"
    ).click()

    expected = "There is no product that matches the search criteria."

    actual = driver.find_element(
        By.XPATH,
        "//input[@id='button-search']/following-sibling::p"
    ).text

    assert actual == expected