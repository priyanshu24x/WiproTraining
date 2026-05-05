#google home page
import time
import pytest_check as check
from selenium import  webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import pytest
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

@pytest.fixture(scope='function')
def driver():
    driver = webdriver.Edge()
    driver.maximize_window()
    driver.get('https://www.google.com/')
    yield driver
    driver.quit()

def test_ghp(driver):
    page_title = driver.title
    assert page_title == 'Google', 'Google Home Page Not Loaded'

def test_imagespageupload(driver):
    driver.find_element(By.LINK_TEXT, 'Images').click()
    pagetitle = driver.title
    assert pagetitle == 'Google Images', 'Images Page Not Loaded'

def test_busienesslink(driver):
    driver.find_element(By.LINK_TEXT, 'Business').click()
    wait = WebDriverWait(driver, 5)
    wait.until(EC.title_contains("Business"))
    # assert 'Business' in driver.title, 'Business Page Not Loaded - Title Check'
    # assert 'business' in driver.current_url, 'Business Page Not Loaded - URL Check'
    check.equal(driver.title, 'Business', 'Business Page Not Loaded - Title Check')
    check.is_in('Business', driver.current_url , 'Business Page Not Loaded - Title Check')
    