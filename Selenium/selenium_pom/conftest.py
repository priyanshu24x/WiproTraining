import pytest
from selenium import  webdriver
from selenium.webdriver.common.by import By

@pytest.fixture(scope='module')
def driver():
    driver = webdriver.Edge()
    driver.maximize_window()
    driver.get('https://www.amazon.in/')
    #driver.find_element(By.XPATH, "//button[text()='Continue shopping']").click()
    yield driver
    driver.quit()
