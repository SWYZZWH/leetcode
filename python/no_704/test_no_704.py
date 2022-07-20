from unittest import TestCase

from no_704 import Solution


class TestSolution(TestCase):
    def test_search(self):
        s = Solution()
        self.assertEqual(3, s.search([2, 0, -1, 3, 6, 8], 3))
        self.assertEqual(0, s.search([2, 0, -1, 3, 6, 8], 2))
        self.assertEqual(2, s.binary_sort([2, 0, -1, 3, 6, 8], -1))
        self.assertEqual(4, s.binary_sort([2, 0, -1, 3, 6, 8], 6))
        self.assertEqual(5, s.binary_sort([2, 0, -1, 3, 6, 8], 8))
