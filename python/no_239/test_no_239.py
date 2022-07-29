from unittest import TestCase

from no_239 import Solution


class Test(TestCase):
    def test_max_sliding_window(self):
        s = Solution()
        self.assertEqual([8, 8, 8], s.maxSlidingWindow([1, 1, 8, 5, 3], 3))
        self.assertEqual([3, 3, 5, 5, 6, 7], s.maxSlidingWindow([1, 3, -1, -3, 5, 3, 6, 7], 3))
