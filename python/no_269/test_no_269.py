from unittest import TestCase

from no_269 import Solution


class TestSolution(TestCase):
    def test_alien_order(self):
        s = Solution()
        self.assertEqual("wertf", s.alienOrder(["wa", "wb", "ce", "cf"]))
