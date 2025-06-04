from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement


class DemoQATextBox:
    FULL_NAME = (By.XPATH, '//input[@id="userName"]')
    EMAIL = (By.XPATH, '//input[@id="userName"]')

    def __init__(self, driver: WebDriver):
        self.driver: WebDriver = driver

    def set_full_name(self, val: str) -> None:
        full_name_element: WebElement = self.driver.find_element(*self.FULL_NAME)
        full_name_element.clear()
        full_name_element.send_keys(val)


