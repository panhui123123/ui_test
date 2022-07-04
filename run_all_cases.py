import pytest

if __name__ == '__main__':
    pytest.main(['-v', './testcases/', '--alluredir=./report/allure-results'])