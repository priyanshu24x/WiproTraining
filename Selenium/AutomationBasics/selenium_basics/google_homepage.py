
from time import sleep

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

browser = input('what browser do you want to use?  ')

match (browser.lower()):
    case 'c':
        chrome_options = Options()
        chrome_options.binary_location = r"C:\Program Files\Google\Chrome Beta\Application\chrome.exe"
        service_obj = Service('../resources/chromedriver.exe')
        driver = webdriver.Chrome(service=service_obj, options=chrome_options)
    case 'e':
        driver = webdriver.Edge(service=Service('../resources/msedgedriver.exe'))
        #service=Service(EdgeChromiumDriverManager().install()))
    case _:
        print('Unknown browser - Not available. \n Executing with default EDGE browser.')
        driver = webdriver.Edge(service=Service('../resources/msedgedriver.exe'))




driver.get("https://www.google.com")

page_title = driver.title

if page_title == 'Google':
    print('Google Homepage loaded - Pass')
else:
    print('Google homepage not loaded - Fail')

sleep(3)

driver.quit()
