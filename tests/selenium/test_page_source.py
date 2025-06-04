import pytest
from selenium.webdriver.common.by import By

def test_launch_browser(driver):
    driver.get("https://demoqa.com/checkbox")
    print(driver.title)
    assert driver.title == "DEMOQA"
    radio_button_locator = "//span[@class='text' and text()='Radio Button']"
    radio_button = driver.find_element(By.XPATH, radio_button_locator)
    radio_button.click()
    expected_url = "https://demoqa.com/radio-button"
    print(f"Current URL is {driver.current_url}")
    assert driver.current_url == expected_url
    page_source = driver.page_source
    print (page_source)

# def test_2(driver):
#     print(f"Current URL is {driver.current_url}")
#     assert driver.title == ""

