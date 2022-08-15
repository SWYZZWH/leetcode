from unittest import TestCase

from no_6132 import Solution


class TestSolution(TestCase):
    def test_minimum_operations(self):
        s = Solution()
        # self.assertEqual(3, s.minimumOperations([1, 5, 0, 3, 5]))
        # self.assertEqual(0, s.minimumOperations([]))
        # self.assertEqual(1, s.minimumOperations([1]))
        # self.assertEqual(2, s.minimumOperations([1, 2]))
        # self.assertEqual(1, s.minimumOperations([2, 2]))
        self.assertEqual(3, s.minimumOperations([1, 1, 1, 2, 2, 2, 3, 3]))
