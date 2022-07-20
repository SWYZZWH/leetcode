from unittest import TestCase

from no_134 import Solution


class TestSolution(TestCase):
    def test_can_complete_circuit(self):
        s = Solution()
        self.assertEqual(3, s.canCompleteCircuit([1, 2, 3, 4, 5], [3, 4, 5, 1, 2]))
        self.assertEqual(-1, s.canCompleteCircuit([2, 3, 4], [3, 4, 3]))
        self.assertEqual(-1, s.canCompleteCircuit([2], [3]))
        self.assertEqual(0, s.canCompleteCircuit([3], [3]))
        self.assertEqual(2, s.canCompleteCircuit([1, 2, 4], [2, 3, 2]))
