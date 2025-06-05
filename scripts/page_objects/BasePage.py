from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement


class BasePage:
    def __init__(self, driver: WebDriver):
        self.driver = driver

    def scroll_into_view(self, element: WebElement):
        self.driver.execute_script(
            "arguments[0].scrollIntoView(true);", element
        )

    def scroll_and_type(self, element: WebElement, val: str):
        self.scroll_into_view(element)
        element.click()
        element.send_keys(val)

    def scroll_and_click(self, element: WebElement):
        self.scroll_into_view(element)
        element.click()

    def wait_for_element_clickable(self, by_locator, timeout=10):
        from selenium.webdriver.support.ui import WebDriverWait
        from selenium.webdriver.support import expected_conditions as EC
        return WebDriverWait(self.driver, timeout).until(EC.element_to_be_clickable(by_locator))

    def wait_for_element_visible(self, by_locator, timeout=10):
        from selenium.webdriver.support.ui import WebDriverWait
        from selenium.webdriver.support import expected_conditions as EC
        return WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(by_locator))

    def safe_click(self, by_locator, timeout=10):
        element = self.wait_for_element_clickable(by_locator, timeout)
        self.scroll_and_click(element)

    def safe_type(self, by_locator, text, timeout=10):
        element = self.wait_for_element_visible(by_locator, timeout)
        self.scroll_and_type(element, text)