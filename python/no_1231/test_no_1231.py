from unittest import TestCase

from no_1231 import Solution


class TestSolution(TestCase):
    def test_maximize_sweetness(self):
        s = Solution()
        self.assertEquals(6, s.maximizeSweetness([1, 2, 3, 4, 5, 6, 7, 8, 9], 5))
