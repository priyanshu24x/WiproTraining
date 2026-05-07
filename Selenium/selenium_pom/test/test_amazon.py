from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from pages.home_page import HomePage


def test_open_amazon(driver):
    assert "amazon" in driver.current_url, 'URL for amazon is not correct'
    assert "Amazon" in driver.title, 'title for amazon is not correct'
    print("\nOpened Amazon Homepage. Title Verified.")

def test_search_product(driver):
    homepage = HomePage(driver)
    homepage.type_search_input()
    homepage.click_search_button()
