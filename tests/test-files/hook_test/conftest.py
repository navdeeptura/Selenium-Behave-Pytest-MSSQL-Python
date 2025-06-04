import pytest
import logging


# @pytest.hookimpl()
def pytest_sessionstart(session):
    logging.info("Session start===============***************")
    print("Session start===============***************")


# @pytest.hookimpl()
def pytest_sessionfinish(session, exitstatus):
    logging.info("Session ends===============***************")
