from unittest import TestCase

from no_2305 import Solution


class TestSolution(TestCase):
    def test_distribute_cookies(self):
        s = Solution()
        self.assertEquals(32, s.distributeCookies([8, 15, 10, 20, 8, 0, 1, 2], 7))
