import pytest
import random


class TestDemo:
    @pytest.mark.run(order=2)
    def test001(self):
        print(111)

    @pytest.mark.run(order=1)
    def test002(self):
        print(222)


if __name__ == '__main__':
    pytest.main(['-s', 'test_999_testDemo.py'])
