from time import sleep

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

def slow_action(delay=1.0):
    sleep(delay)


@pytest.mark.sele
def test_launch_website():
    service = Service(executable_path="drivers/chromedriver.exe")
    driver = webdriver.Chrome(service=service)
    driver.implicitly_wait(5)

    driver.get("http://localhost:5192/")
    assert "Login" in driver.title

    username = driver.find_element(By.XPATH, "//input[@name='username']")
    username.send_keys("raman")
    password = driver.find_element(By.XPATH, "//input[contains(@type, 'password')]")
    password.send_keys("raman")
    password.clear()
    password.send_keys("raman")
    #password.send_keys(Keys.RETURN)
    login_button = driver.find_element(By.CSS_SELECTOR, "button.btn.btn-primary.w-100")
    login_button.click()
    print (driver.title, driver.dialog, driver.current_url)
    assert driver.title == "Home - ERPSystem"

    slow_action(2)
    driver.execute_script("window.open('');")
    driver.switch_to.window(driver.window_handles[1])
    slow_action()
    driver.get("http://localhost:5192/Home/Privacy")
    slow_action()
    assert driver.title == "Privacy Policy - ERPSystem"
    slow_action(2)
    driver.switch_to.window(driver.window_handles[0])
    slow_action(2)
    driver.switch_to.window(driver.window_handles[1])
    slow_action(2)
    driver.close()
    slow_action(5)
    driver.quit()
