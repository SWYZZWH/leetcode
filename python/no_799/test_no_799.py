from unittest import TestCase

from no_799 import Solution

class TestSolution(TestCase):
    def test_champagne_tower(self):
        s = Solution()
        # self.assertEqual(0, s.champagneTower(0, 0, 0))
        # self.assertEqual(0.25, s.champagneTower(4, 2, 0))
        # self.assertEqual(0.5, s.champagneTower(4, 2, 1))
        self.assertEqual(1.0, s.champagneTower(10, 3, 1))
