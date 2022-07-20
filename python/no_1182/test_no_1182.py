from unittest import TestCase

from no_1182 import Solution


class TestSolution(TestCase):
    def test_shortest_distance_color(self):
        s = Solution()
        self.assertEqual([3, 0, 3], s.shortestDistanceColor([1, 1, 2, 1, 3, 2, 2, 3, 3], [[1, 3], [2, 2], [6, 1]]))
