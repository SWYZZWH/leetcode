from unittest import TestCase

from no_1354 import Solution


class TestSolution(TestCase):
    def test_is_possible(self):
        s = Solution()
        # self.assertEqual(True, s.isPossible([1, 1000000000]))
        # self.assertEqual(True, s.isPossible([9, 5, 3]))
        # self.assertEqual(True, s.isPossible([1, 5, 1]))
        # self.assertEqual(True, s.isPossible([1, 5, 7]))
        # self.assertEqual(True, s.isPossible([1]))
        self.assertEqual(False, s.isPossible([1, 1, 1, 2]))
