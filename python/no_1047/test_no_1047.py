from unittest import TestCase

from no_1047 import Solution


class TestSolution(TestCase):
    def test_remove_duplicates(self):
        s = Solution()
        self.assertEqual("a", s.removeDuplicates("a"))
        self.assertEqual("ab", s.removeDuplicates("ab"))
        self.assertEqual("ab", s.removeDuplicates("bbab"))
        self.assertEqual("", s.removeDuplicates("aacc"))
        self.assertEqual("", s.removeDuplicates("accbaaba"))
        self.assertEqual("", s.removeDuplicates("affcca"))
        self.assertEqual("ibfjcdidiaidchakchchcahabhibdcejkdkfbecdjhajbkfebebfea", s.removeDuplicates("ibfjcaffccadidiaidchakchchcahabhibdcejkdkfbaeeaecdjhajbkfebebfea"))
