from unittest import TestCase

from no_10 import Solution


class TestSolution(TestCase):
    def test_is_match(self):
        s = Solution()
        self.assertEqual(True, s.isMatch("aa", "a*"))
        self.assertEqual(True, s.isMatch("aa", ".*"))
        self.assertEqual(True, s.isMatch("aa", ".*.*"))
        self.assertEqual(True, s.isMatch("aa", ".*a.*"))
        self.assertEqual(False, s.isMatch("aa", ".*b.*"))
        self.assertEqual(False, s.isMatch("aac", "b*c"))
        self.assertEqual(True, s.isMatch("bbcc", "b*c*"))
        self.assertEqual(True, s.isMatch("", "b*c*"))
        self.assertEqual(True, s.isMatch("", ".*"))
        self.assertEqual(False, s.isMatch("", "."))
        self.assertEqual(True, s.isMatch("a", "."))
        self.assertEqual(False, s.isMatch("aa", "."))
        self.assertEqual(True, s.isMatch("aa", ".."))
        self.assertEqual(True, s.isMatch("aaa", "..a"))
        self.assertEqual(False, s.isMatch("aa", "..a"))
        self.assertEqual(False, s.isMatch("a", "..a"))
        self.assertEqual(False, s.isMatch("aaaa", "..a"))
        self.assertEqual(True, s.isMatch("bcadsf", "b*.*"))
        self.assertEqual(False, s.isMatch("bcadsfdsfdsfsfdsf", "b*.*.*.*.*m.*a.*.*f.*s.*"))
        self.assertEqual(False, s.isMatch("a", "ab*a"))
        self.assertEqual(False, s.isMatch("a", ".*..a*"))
