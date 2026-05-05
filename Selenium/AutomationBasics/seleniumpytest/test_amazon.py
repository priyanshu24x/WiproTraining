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
    driver.get('https://www.amazon.in/')
    driver.find_element(By.XPATH, "//button[text()='Continue shopping']").click()
    yield driver
    driver.quit()

def test_open_amazon(driver):
    assert "amazon" in driver.current_url, 'URL for amazon is not correct'
    assert "Amazon" in driver.title, 'title for amazon is not correct'
    print("\nOpened Amazon Homepage. Title Verified.")

def test_search_product(driver):
    wait = WebDriverWait(driver, 5)
    search_box = wait.until(EC.presence_of_element_located((By.NAME, "field-keywords")))
    search_box.clear()
    search_box.send_keys("wireless mouse")

    search_button = driver.find_element(By.ID, "nav-search-submit-button")
    search_button.click()

    assert driver.current_url.__contains__('wireless'), 'Search result page did not load'
    assert driver.title.__contains__('wireless'), 'Search result page did not load'
    print("\nSearch results page loaded successfully")

def test_find_elements_amazon(driver):
    wait = WebDriverWait(driver,15)

    first_product = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "a h2 span")))
    print("\nFirst Product: ", first_product)
    product_titles = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "a h2 span")))
    print(f"\nFound {len(product_titles)} product titles on page one.\n")

    for i, title in enumerate(product_titles[:5], start=1):
        print(f"{i}. {title.text}")

    assert len(product_titles) > 0, "No products found on amazon search results"