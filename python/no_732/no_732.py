from sortedcontainers import SortedDict


class MyCalendarThree:

    def __init__(self):
        self.sd = SortedDict()

    def book(self, start: int, end: int) -> int:
        self.sd[start] = self.sd.get(start, 0) + 1
        self.sd[end] = self.sd.get(end, 0) - 1
        res = 0
        cur = 0
        for v in self.sd.values():
            cur += v
            res = max(res, cur)

        return res

# Your MyCalendarThree object will be instantiated and called as such:
# obj = MyCalendarThree()
# param_1 = obj.book(start,end)