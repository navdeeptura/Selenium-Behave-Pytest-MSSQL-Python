import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.remote.webdriver import WebDriver
from webdriver_manager.chrome import ChromeDriverManager

from scripts.page_objects.DemoQATextBox import DemoQATextBox


class TestDemoQATextBox:

    def test_open_url_and_enter_valid_credentials(self):
        driver2: WebDriver = webdriver.Chrome(
            service=Service(ChromeDriverManager().install())
        )


        driver2.get("https://demoqa.com/text-box")

        text_box_page = DemoQATextBox(driver2)
        text_box_page.set_full_name("Navdeep T")

        time.sleep(5)
        assert "DEMOQA" in driver2.title

    def test_open_url_with_conftest_browser(self, driver: WebDriver):
        driver2 = webdriver.Chrome(
            service=Service(ChromeDriverManager().install())
        )
        driver.get("https://demoqa.com/text-box")

        text_box_page = DemoQATextBox(driver)
        text_box_page.set_full_name("Navdeep T")

        assert "DEMOQA" in driver.title
        driver2.quit()