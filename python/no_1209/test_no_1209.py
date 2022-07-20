from unittest import TestCase

from no_1209 import Solution


class TestSolution(TestCase):
    def test_remove_duplicates(self):
        s = Solution()
        self.assertEqual("abcd", s.removeDuplicates("abcd", 2))
        self.assertEqual("aa", s.removeDuplicates("deeedbbcccbdaa", 3))
        self.assertEqual("ps", s.removeDuplicates("pippis", 2))
        self.assertEqual("ps", s.removeDuplicates("pbbcggttciiippooaais", 2))
