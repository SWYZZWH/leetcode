from unittest import TestCase

from no_1675 import Solution


class TestSolution(TestCase):
    def test_minimum_deviation(self):
        s = Solution()
        self.assertEqual(1, s.minimumDeviation([1, 2, 3, 4]))
        self.assertEqual(3, s.minimumDeviation([4, 1, 5, 20, 3]))
        self.assertEqual(3, s.minimumDeviation([2, 10, 8]))
