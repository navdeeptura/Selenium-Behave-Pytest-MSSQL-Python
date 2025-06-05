import time

import pytest
import yaml
from pathlib import Path
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.remote.webdriver import WebDriver
from webdriver_manager.chrome import ChromeDriverManager

from scripts.page_objects.DemoQATextBox import DemoQATextBox


class TestDemoQATextBox:
    url = "https://demoqa.com/text-box"

    @pytest.mark.selenium
    def test_open_url_and_enter_valid_credentials(self):
        driver2: WebDriver = webdriver.Chrome(
            service=Service(ChromeDriverManager().install())
        )
        driver2.get("https://demoqa.com/text-box")

        text_box_page = DemoQATextBox(driver2)
        text_box_page.set_full_name("Navdeep T")

        time.sleep(5)
        assert "DEMOQA" in driver2.title

    @pytest.mark.current
    @pytest.mark.selenium
    def test_open_url_with_conftest_browser(self, driver: WebDriver, textbox_test_data):
        user = textbox_test_data[0]
        driver.get("https://demoqa.com/text-box")

        assert "DEMOQA" in driver.title

        text_box_page = DemoQATextBox(driver)

        text_box_page.set_full_name(user["full_name"])
        text_box_page.set_email(user["email"])
        text_box_page.set_current_address(user["address"])
        text_box_page.click_submit_button()

        time.sleep(5)

    @pytest.mark.selenium
    def test_browser_check(self):
        driver = webdriver.Chrome(
            service=Service(ChromeDriverManager().install())
        )
        driver.get(self.url)
        driver.quit()