from unittest import TestCase

from no_2104 import Solution


class TestSolution(TestCase):
    def test_sub_array_ranges(self):
        s = Solution()
        self.assertEqual(4, s.subArrayRanges([1, 3, 3]))
        self.assertEqual(13, s.subArrayRanges([3, 1, 2, 4]))
        self.assertEqual(4, s.subArrayRanges([1, 2, 3]))
        self.assertEqual(0, s.subArrayRanges([1]))
        self.assertEqual(1, s.subArrayRanges([1, 2]))
        self.assertEqual(24, s.subArrayRanges([2, 5, 8, 5]))
