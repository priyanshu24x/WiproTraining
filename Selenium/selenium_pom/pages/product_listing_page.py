from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webdriver import WebDriver
import time

class ProductListPage:
    PRODUCT_TITLES = (By.CSS_SELECTOR, "a h2 span")
    BRAND_FILTER = (By.XPATH, "//span[text()='Logitech']")

    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

    def find_product_title(self):
        first_product = self.wait.until(EC.presence_of_element_located(self.PRODUCT_TITLES))
        print("\nFirst Product: ", first_product.text)

    def all_products(self):
        product_titles = self.wait.until(EC.presence_of_all_elements_located(self.PRODUCT_TITLES))
        print(f"\nFound {len(product_titles)} product titles in page one \n")

        for i, title in enumerate(product_titles[:5], start=1):
            print(f"{i}, {title.text}")

        return len(product_titles) >0

    def select_brand_filter(self):
        brand_filter = self.driver.find_element(*self.BRAND_FILTER)
        brand_filter.click()

    def check_product_titles_for_brand_filter(self,brand_name):
        self.wait.until(EC.presence_of_all_elements_located(self.PRODUCT_TITLES))
        time.sleep(2)
        product_titles = self.driver.find_elements(*self.PRODUCT_TITLES)
        mismatches=[]

        for title in product_titles[:10]:
           text = title.text.lower()
           if "sponsored" not in text and brand_name.lower() not in text:
                mismatches.append(title.text)
                print(f"real failure: {title.text}")
        return len(mismatches) <3
