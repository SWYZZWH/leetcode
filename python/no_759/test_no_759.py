from unittest import TestCase

from no_759 import Solution
from no_759 import Interval


class TestSolution(TestCase):
    def test_employee_free_time(self):
        s = Solution()
        self.assertEqual(Interval(3, 4), s.employeeFreeTime([[Interval(1, 2), Interval(5, 6)], [Interval(1, 3)], [Interval(4, 10)]]))
