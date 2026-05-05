import time
from selenium import  webdriver
from selenium.webdriver.common.by import By
import pytest


@pytest.fixture(scope='module')
def driver():
    driver = webdriver.Edge()
    driver.maximize_window()
    driver.get('https://the-internet.herokuapp.com/javascript_alerts')
    yield driver
    driver.quit()

def test_simlpe_js_alert(driver):
    driver.find_element(By.XPATH,"//button[text()='Click for JS Alert']").click()
    alert = driver.switch_to.alert
    assert alert.text == "I am a JS Alert", "alert text wa wrong"
    time.sleep(3)
    alert.accept()
    time.sleep(3)
    result = driver.find_element(By.ID, "result").text
    assert "You successfully clicked an alert" in result, 'result text was wrong'

def test_js_confirmdismiss(driver):
    driver.find_element(By.XPATH, "//button[text()='Click for JS Confirm']").click()
    alert = driver.switch_to.alert
    assert alert.text == "I am a JS Confirm", "alert text wa wrong"
    time.sleep(3)
    alert.dismiss() #cancel
    time.sleep(3)
    result = driver.find_element(By.ID, "result").text
    assert "You clicked: Cancel" in result, 'result text was wrong'

def test_js_confirmok(driver):
    driver.find_element(By.XPATH, "//button[text()='Click for JS Confirm']").click()
    alert = driver.switch_to.alert
    assert alert.text == "I am a JS Confirm", "alert text wa wrong"
    time.sleep(3)
    alert.accept()
    time.sleep(3)
    result = driver.find_element(By.ID, 'result').text
    assert "You clicked: Ok" in result

def test_js_prompt(driver):
    driver.find_element(By.XPATH, "//button[text()='Click for JS Prompt']").click()
    alert = driver.switch_to.alert
    time.sleep(3)
    assert alert.text == "I am a JS prompt"

    alert.send_keys("Python Selenium")
    time.sleep(3)
    alert.accept()
    time.sleep(3)

    result = driver.find_element(By.ID, "result").text
    assert "Python Selenium" in result