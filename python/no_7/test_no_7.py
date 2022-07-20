from unittest import TestCase
from no_7 import Solution


class TestSolution(TestCase):
    def test_check_overflow(self):
        s = Solution()
        self.assertEqual(321, s.reverse(123))
        self.assertEqual(-321, s.reverse(-123))
        self.assertEqual(21, s.reverse(120))
        self.assertEqual(1, s.reverse(1))
        self.assertEqual(-1, s.reverse(-1))
        self.assertEqual(-1111, s.reverse(-1111))
        self.assertEqual(-1, s.reverse(-1000))
        self.assertEqual(0, s.reverse(4294967296))
