from unittest import TestCase

from no_1268 import Solution


class TestSolution(TestCase):
    def test_suggested_products(self):
        s = Solution()
        print(s.suggestedProducts(["mobile","mouse","moneypot","monitor","mousepad"], "mouse"))