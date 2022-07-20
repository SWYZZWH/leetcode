from unittest import TestCase

from no_2272 import Solution


class TestSolution(TestCase):
    def test_largest_variance(self):
        s = Solution()
        self.assertEqual(2, s.largestVariance("abbabaaba"))
