import unittest

from no_33 import Solution


class MyTestCase(unittest.TestCase):
    def test_something(self):
        s = Solution()
        # self.assertEqual(4, s.search([4, 5, 6, 7, 0, 1, 2], 0))
        # self.assertEqual(-1, s.search([4, 5, 6, 7, 0, 1, 2], 3))
        # self.assertEqual(-1, s.search([4, 5, 6, 7, 0, 1, 2], 9))
        # self.assertEqual(3, s.search([4, 5, 6, 7, 0, 1, 2], 7))
        # self.assertEqual(0, s.search([1], 1))
        # self.assertEqual(-1, s.search([1], 0))
        # self.assertEqual(-1, s.search([1], 3))
        # self.assertEqual(2, s.search([1, 2, 3], 3))
        # self.assertEqual(-1, s.search([5, 1, 3], 0))
        self.assertEqual(1, s.search([2, 3, 4, 5, 6, 7, 8, 1], 3))


if __name__ == '__main__':
    unittest.main()
