from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from pages.home_page import HomePage
from pages.product_listing_page import ProductListPage


def test_open_amazon(driver):
    assert "amazon" in driver.current_url, 'URL for amazon is not correct'
    assert "Amazon" in driver.title, 'title for amazon is not correct'
    print("\nOpened Amazon Homepage. Title Verified.")

def test_search_product(driver):
    homepage = HomePage(driver)
    homepage.type_search_input()
    homepage.click_search_button()

    assert homepage.is_amazon_loaded()== True , 'Search results page did not load'
    print("\nSearch results page loaded successfully")

def test_find_elements_amazon(driver):
    product_listing_page = ProductListPage(driver)
    val = product_listing_page.all_products()

    assert val, "No products found on Amazon search results"

def test_brand_filter(driver):
    product_listing_page = ProductListPage(driver)

    product_listing_page.select_brand_filter()

    assert product_listing_page.check_product_titles_for_brand_filter('Logitech'), 'Brand filter did not apply'
