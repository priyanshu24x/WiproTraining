from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
#from webdriver_manager.chrome import Doc
import time

#start driver
driver = webdriver.Edge()   #servive=Service('../resources/msedgedriver.exe')
driver.maximize_window()

driver.get("https://www.selenium.dev/selenium/web/web-form.html")
time.sleep(1)

#text input
text_input = driver.find_element(By.ID, "my-text-id")
text_input.clear()
text_input.send_keys("Selenium Webdriver Demo")

#password
password_input = driver.find_element(By.NAME, "my-password")
password_input.clear()
password_input.send_keys("secret123")

#textarea
textarea = driver.find_element(By.NAME, "my-textarea")
textarea.clear()
textarea.send_keys("Thus is a sample message")

#checkbox
checkbox = driver.find_element(By.ID,"my-check-2")
checkbox.click()

#radiobutton
radio = driver.find_element(By.ID, "my-radio-2")
radio.click()

#dropdown
dropdown = driver.find_element(By.NAME, "my-select")
dropdown.click()
option = driver.find_element(By.CSS_SELECTOR, "select[name='my-select'] option[value='2']")
option.click()

#multiselect
multi_select = driver.find_element(By.NAME, "my-datalist")
multi_select.send_keys("New York")

#file upload
file_upload = driver.find_element(By.NAME, "my-file")
file_upload.send_keys("C:\\Wipro Training\\Python\\PythonCoding\\daily_assignments\\day1_Q2..txt") #use any valid path on ur pc

#range slider
range_slider = driver.find_element(By.NAME, "my-range")
driver.execute_script("arguments[0], value = 10;", range_slider) #set driver value

#colorpicker
color_picker = driver.find_element(By.NAME, "my-colors")
color_picker.send_keys("#00ff00") #green

#datepicker
date_input = driver.find_element(By.NAME, "my-date")
date_input.send_keys("2025-12-25")

#sumitbutton
submit_btn = driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
time.sleep(3)
submit_btn.click()


time.sleep(3)
driver.quit()