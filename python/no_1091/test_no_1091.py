from unittest import TestCase

from no_1091 import Solution


class TestSolution(TestCase):
    def test_shortest_path_binary_matrix(self):
        s = Solution()
        self.assertEqual(2, s.shortestPathBinaryMatrix([[0, 1], [1, 0]]))
        self.assertEqual(-1, s.shortestPathBinaryMatrix([[0, 1], [1, 1]]))
        self.assertEqual(-1, s.shortestPathBinaryMatrix([[1, 1], [1, 0]]))
        self.assertEqual(4, s.shortestPathBinaryMatrix([[0, 0, 0], [1, 1, 0], [1, 1, 0]]))
        self.assertEqual(-1, s.shortestPathBinaryMatrix([[1, 0, 0], [1, 1, 0], [1, 1, 0]]))
