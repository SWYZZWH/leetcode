from unittest import TestCase

from no_41 import Solution


class TestSolution(TestCase):
    def test_first_missing_positive(self):
        s = Solution()
        # self.assertEqual(2, s.firstMissingPositive([3, 4, -1, 1]))
        self.assertEqual(1, s.firstMissingPositive([3, 4, 0, 2]))
