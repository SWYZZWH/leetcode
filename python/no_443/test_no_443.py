from unittest import TestCase

from no_443 import Solution


class TestSolution(TestCase):
    def test_compress(self):
        s = Solution()
        # self.assertEqual(4, s.compress(["a", "a", "b", "b"]))
        # self.assertEqual(6, s.compress(["a", "a", "b", "b", "c", "c", "c"]))
        # self.assertEqual(1, s.compress(["a"]))
        # self.assertEqual(2, s.compress(["a", "a"]))
        self.assertEqual(3, s.compress(["a", "b", "a"]))
        # self.assertEqual(5, s.compress(["a", "a", "a", "c", "c", "c", "c", "c", "c", "c", "c", "c", "c", "c", "c"]))
        self.assertEqual(3, s.compress(["a", "a", "a", "a", "a", "b"]))
