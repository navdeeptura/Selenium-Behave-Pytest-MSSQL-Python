import logging
import sys
import os
import yaml
from pathlib import Path

import pytest

project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
if project_root not in sys.path:
    sys.path.insert(0, project_root)

from scripts.utils.browser_manager import get_driver

def pytest_addoption(parser):
    parser.addoption("--browser",
                     action="store",
                     default="chrome",
                     help="Browser to run tests")
    parser.addoption("--headless",
                     action="store_true",
                     help="Run browser in headless mode")


@pytest.fixture(scope='function')
def driver(request):
    browser = request.config.getoption("--browser")
    headless = request.config.getoption("--headless")
    driver = get_driver(browser, headless)
    driver.maximize_window()
    yield driver
    driver.quit()


from config.setup_logger import setup_logger

@pytest.fixture(scope="session", autouse=True)
def configure_logging():
    """This fixture is to initiate logger at start of session"""
    log_level = logging.WARNING
    log_path = os.path.join(project_root, "logs.log")

    #clean previous log files
    open(log_path, 'w').close()

    setup_logger(log_level, log_path)
    logging.info("Logger started in root-conftest.py file")
    logging.info("Logger initiated for the Automation")


@pytest.fixture(scope="session")
def textbox_test_data():
    data_file = Path(__file__).parent.parent / "test_data" / "user_information.yaml"
    with open(data_file, "r") as f:
        data = yaml.safe_load(f)
    return data["test_users"]

