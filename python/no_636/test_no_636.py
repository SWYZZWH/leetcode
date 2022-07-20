from unittest import TestCase

from no_636 import Solution


class TestSolution(TestCase):
    def test_rec(self):
        s = Solution()
        # self.assertEquals([3, 4], s.exclusiveTime(2, ["0:start:0", "1:start:2", "1:end:5", "0:end:6"]))
        # self.assertEquals([8], s.exclusiveTime(1, ["0:start:0", "0:start:2", "0:end:5", "0:start:6", "0:end:6", "0:end:7"]))
        self.assertEquals([6], s.exclusiveTime(1, ["0:start:0", "0:start:1", "0:start:2", "0:end:3", "0:end:4", "0:end:5"]))
        self.assertEquals([1, 1, 2], s.exclusiveTime(3, ["0:start:0", "0:end:0", "1:start:1", "1:end:1", "2:start:2", "2:end:2", "2:start:3", "2:end:3"]))
