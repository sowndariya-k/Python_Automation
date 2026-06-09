import pytest
from selenium import webdriver
import read_config


@pytest.fixture()
def setup_and_teardown(request):
    browser=read_config.get_config("basic info", "browser")
    if browser.lower()=="chrome":
        driver=webdriver.Chrome()
    else:
        raise Exception("Unsupported Browser")
    driver.maximize_window()

    url=read_config.get_config("basic info", "url")
    driver.get(url)
    request.cls.driver=driver

    yield
    driver.quit()