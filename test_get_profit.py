"""
    Test cases for the profit.py file
    It covers the following cases, call the get_profit method with various combinations
    Case 1: movie type = 1
    Case 2: movie type = 2
    Case 3: movie type = 3
"""
from unittest import TestCase

from profit import get_profit


class TestProfit(TestCase):
    def test_get_profit_case1(self):
        assert get_profit(100000, 1) == 30000

    def test_get_profit_case2(self):
        assert get_profit(100000, 2) == 20000

    def test_get_profit_case3(self):
        assert get_profit(100000, 3) == 10000
