from unittest import TestCase

from no_631 import Excel


class Test(TestCase):
    def test_excel(self):
        s = Excel(3, "C")
        s.set(1, "A", 2)
        print(s.sum(3, "C", ["A1", "A1:B2"]))
        s.set(2, "B", 2)
        print(s.get(3, "C"))

        s = Excel(5, "E")
        s.set(1, "A", 1)
        print(s.sum(2, "B", ["A1"]))
        s.set(2, "B", 0)
        s.set(1, "A", 5)
        print(s.get(2, "B"))

        # ["Excel", "set", "sum", "set", "get", "set", "get"]
        # [[5, "E"], [1, "A", 1], [2, "B", ["A1"]], [2, "B", 0], [2, "B"], [1, "A", 5], [2, "B"]]

