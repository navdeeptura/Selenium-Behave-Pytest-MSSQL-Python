import logging

import pytest


def test_1_print():
    """This is the sample test, always start with or ends with test"""
    logging.info("executing test_1_print")

@pytest.mark.current
class TestSampleClass:
    """This is the sample class, Class Name should always start with Test"""
    value = 0

    def test_2_print(self):
        """Sample method in the class"""
        logging.info("test 2 print")
        assert self.value == 0, "Expected - 0"

    def test_needs_files(self, tmp_path):
        with pytest.raises(Exception) as exp:
            print (tmp_path)
            assert 0 == 0
            raise ValueError("Invalid Values")
        assert str(exp.value) == "Invalid Values"

