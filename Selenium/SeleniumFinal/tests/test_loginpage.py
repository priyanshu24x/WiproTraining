import pytest
from pages.loginpage import LoginPage
from utils.csv_reader import CSVReader

from utils.excel_reader import ExcelReader

from pages.basepage import logger
from utils.logger import LogGen
from utils.screenshot import ScreenshotUtil

logger = LogGen.loggen()

@pytest.mark.order(1)
@pytest.mark.parametrize(
    "data",
    CSVReader.read_csv("login_data.csv")
    # ExcelReader.read_excel("test_data.xlsx", "login_data")
)
def test_login(driver, data):
    login_page = LoginPage(driver)
    logger.info(f"loggin page opened")
    logger.info(f"trying to login with username: {data['username']} and password: {data['password']}")
    login_page.login(data["username"], data["password"])

    logger.info(f"checking if login is successful")
    if data["expected_result"] == "success":
        assert "inventory" in driver.current_url
        logger.info(f"login is successful - inventory page opened")
        screensoth_path = ScreenshotUtil.capture_screenshot(driver, screenshot_name="login_text")
    else:
        assert "inventory" not in driver.current_url
        assert login_page.read_error_message().__contains__("do not match")
        logger.error(f"login is unsuccessful - inventory page not opened")
        screensoth_path = ScreenshotUtil.capture_screenshot(driver, screenshot_name="login_text")