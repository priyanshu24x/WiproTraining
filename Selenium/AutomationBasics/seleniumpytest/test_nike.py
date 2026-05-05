import time
from selenium import  webdriver
from selenium.webdriver.common.by import By
import pytest
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

@pytest.fixture(scope='module')
def driver():
    driver = webdriver.Edge()
    driver.maximize_window()
    driver.get('https://www.nike.in/')
    yield driver
    driver.quit()

def test_open_nike(driver):
    assert "nike" in driver.current_url, 'URL for nike is not correct'
    assert "nike" in driver.title, 'title for nike is not correct'
    print("\nOpened nike Homepage. Title Verified.")