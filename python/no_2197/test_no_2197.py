from unittest import TestCase

from no_2197 import Solution


class TestSolution(TestCase):
    def test_replace_non_coprimes(self):
        s = Solution()
        self.assertEqual([2009, 20677, 825], s.replaceNonCoprimes([287, 41, 49, 287, 899, 23, 23, 20677, 5, 825]))
