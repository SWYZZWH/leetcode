from unittest import TestCase

from no_135 import Solution


class TestSolution(TestCase):
    def test_candy(self):
        s = Solution()
        # self.assertEqual(5, s.candy([1, 0, 2]))
        # self.assertEqual(4, s.candy([1, 2, 2]))
        self.assertEqual(12, s.candy([29, 51, 87, 87, 72, 12]))
