from unittest import TestCase

from no_465 import Solution


class TestSolution(TestCase):
    def test_min_transfers(self):
        s = Solution()
        self.assertEqual(2, s.minTransfers([[0, 1, 10], [2, 0, 5]]))
