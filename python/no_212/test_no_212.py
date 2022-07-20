from unittest import TestCase

from no_212 import Solution


class TestSolution(TestCase):
    def test_dfs(self):
        s = Solution()
        self.assertEquals(["a"], s.findWords([["o", "a", "a", "n"], ["e", "t", "a", "e"], ["i", "h", "k", "r"], ["i", "f", "l", "v"]], ["a"]))
        self.assertEquals(["o", "a", "k", "v"], s.findWords([["o", "a", "a", "n"], ["e", "t", "a", "e"], ["i", "h", "k", "r"], ["i", "f", "l", "v"]], ["o", "a", "k", "v", "m"]))
        self.assertEquals(["o", "oa", "oaa"], s.findWords([["o", "a", "a", "n"], ["e", "t", "a", "e"], ["i", "h", "k", "r"], ["i", "f", "l", "v"]], ["oaa", "oa", "o"]))
        self.assertEquals(["oath", "eat"], s.findWords([["o", "a", "a", "n"], ["e", "t", "a", "e"], ["i", "h", "k", "r"], ["i", "f", "l", "v"]], ["oath", "pea", "eat", "rain"]))
