from unittest import TestCase

from no_752 import Solution


class TestSolution(TestCase):
    def test_open_lock(self):
        s = Solution()
        self.assertEqual(0, s.openLock([], "0000"))
        self.assertEqual(1, s.openLock(["0001"], "0009"))
        self.assertEqual(6, s.openLock(["0201", "0101", "0102", "1212", "2002"], "0202"))
        self.assertEqual(-1, s.openLock(["8887", "8889", "8878", "8898", "8788", "8988", "7888", "9888"], "8888"))
