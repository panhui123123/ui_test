import pytest
import random


class TestDemo:
    def test_001(self):
        print(111)

    def test_002(self):
        print(222)


if __name__ == '__main__':
    pytest.main(['-s', 'test_999_testDemo.py'])
