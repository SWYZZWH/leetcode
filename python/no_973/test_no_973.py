from unittest import TestCase

from no_973 import Solution


class TestSolution(TestCase):
    def test_k_closest(self):
        s = Solution()
        self.assertEqual([[-2, 2]], s.kClosest([[1, 3], [-2, 2]], 1))
