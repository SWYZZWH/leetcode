from unittest import TestCase

from no_6135 import Solution


class TestSolution(TestCase):
    def test_longest_cycle(self):
        s = Solution()
        # self.assertEqual(3, s.longestCycle([3, 3, 4, 2, 3]))
        self.assertEqual(4, s.longestCycle([1, 2, 0, 4, 5, 6, 3, 8, 9, 7]))
