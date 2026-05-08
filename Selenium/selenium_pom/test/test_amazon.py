from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import pytest
from pages.home_page import HomePage
from pages.product_listing_page import ProductListPage


def test_open_amazon(driver):
    assert "amazon" in driver.current_url, 'URL for amazon is not correct'
    assert "Amazon" in driver.title, 'title for amazon is not correct'
    print("\nOpened Amazon Homepage. Title Verified.")

@pytest.mark.parametrize("search_product", [("wireless mouse"), ("shoes")])

def test_search_product(driver, search_product):
    homepage = HomePage(driver)
    homepage.type_search_input(search_product)
    print(f"Searching product - {search_product}")
    homepage.click_search_button()

    assert homepage.is_amazon_loaded()== True , 'Search results page did not load'
    print("\nSearch results page loaded successfully")

@pytest.mark.parametrize("search_product", [("wireless mouse"), ("shoes")])

def test_find_elements_amazon(driver, search_product):
    homepage = HomePage(driver)
    homepage.type_search_input(search_product)
    homepage.click_search_button()

    assert homepage.is_amazon_loaded(), 'Search page did not load.'
    print("\nSesrch resu:ts page loaded successfully")

    productlistingpage = ProductListPage(driver)
    productlistingpage.find_product_title()
    val = productlistingpage.all_products()

    assert  val, "No products found on amazon search results"

@pytest.mark.parametrize("search_product", [("wireless mouse", "Logitech"), ("shoes", "NIke")])


def test_brand_filter(driver, search_product, brandname):
    homepage = HomePage(driver)
    homepage.type_search_input(search_product)
    print(f"\nSearch results page loaded successfully - {search_product}")
    homepage.click_search_button()

    assert homepage.is_amazon_loaded(), 'Search results page did not load'
    print(f"\nSearch results page loaded succesfully - {search_product}")

    productlistingpage = ProductListPage(driver)

    productlistingpage.select_brand_filter(brandname)

    assert productlistingpage.check_product_titles_for_brand_filter(brandname), 'Brand filter did not apply'
