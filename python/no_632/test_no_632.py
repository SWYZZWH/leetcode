from unittest import TestCase

from no_632 import Solution


class TestSolution(TestCase):
    def test_smallest_range(self):
        s = Solution()
        self.assertEqual([20, 24], s.smallestRange([[4, 10, 15, 24, 26], [0, 9, 12, 20], [5, 18, 22, 30]]))
        self.assertEqual([1, 1], s.smallestRange([[1, 2, 3], [1, 2, 3], [1, 2, 3]]))
        self.assertEqual([10, 11], s.smallestRange([[10, 10], [11, 11]]))
