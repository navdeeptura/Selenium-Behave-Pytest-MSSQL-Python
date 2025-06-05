from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement

from scripts.page_objects.BasePage import BasePage


class DemoQATextBox(BasePage):
    FULL_NAME = (By.XPATH, '//input[@id="userName"]')
    EMAIL = (By.XPATH, "//input[@id='userEmail']")
    CURRENT_ADDRESS = (By.XPATH, "//textarea[@id='currentAddress']")
    SUBMIT_BUTTON = (By.XPATH, "//button[@id='submit']")

    def __init__(self, driver: WebDriver):
        super().__init__(driver)
        self.driver: WebDriver = driver

    def set_full_name(self, val: str) -> None:
        full_name_element: WebElement = self.driver.find_element(*self.FULL_NAME)
        self.scroll_and_type(full_name_element, val)

    def set_email(self, val:str) -> None:
        email_element: WebElement = self.driver.find_element(*self.EMAIL)
        self.scroll_and_type(email_element, val)

    def set_current_address(self, val:str) -> None:
        curr_address_element = self.driver.find_element(*self.CURRENT_ADDRESS)
        self.scroll_and_type(curr_address_element, val)

    def click_submit_button(self) -> None:
        submit_button_element = self.driver.find_element(*self.SUBMIT_BUTTON)
        self.scroll_and_click(submit_button_element)


