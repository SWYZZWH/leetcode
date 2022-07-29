from unittest import TestCase

from no_1405 import Solution


class TestSolution(TestCase):
    def test_longest_diverse_string(self):
        s = Solution()
        self.assertEqual("ccbccaccbccaabbccaabbcc", s.longestDiverseString(5, 6, 12))
