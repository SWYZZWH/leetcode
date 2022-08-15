from unittest import TestCase

from no_6134 import Solution


class TestSolution(TestCase):
    def test_closest_meeting_node(self):
        s = Solution()
        self.assertEqual(2, s.closestMeetingNode([2, 2, 3, -1], 0, 1))
        self.assertEqual(2, s.closestMeetingNode([1, 2, -1], 0, 2))
        self.assertEqual(0, s.closestMeetingNode([2, 0, 0], 0, 2))
