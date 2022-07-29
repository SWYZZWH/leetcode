from unittest import TestCase

from no_1235 import Solution


class TestSolution(TestCase):
    def test_job_scheduling(self):
        s = Solution()
        self.assertEqual(120, s.jobScheduling([2, 1, 3, 3]
                                              , [4, 3, 5, 6]
                                              , [10, 50, 40, 70]))
