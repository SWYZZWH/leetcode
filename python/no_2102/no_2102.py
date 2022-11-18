from sortedcontainers import SortedList


# two heap solution is elegant
# it inspires us to use heap solve problems like median and kth element
class SORTracker:

    def __init__(self):
        self.sl = SortedList()
        self.counter = 0

    def add(self, name: str, score: int) -> None:
        self.sl.add((-score, name))

    def get(self) -> str:
        res = self.sl[self.counter][1]
        self.counter += 1
        return res

# Your SORTracker object will be instantiated and called as such:
# obj = SORTracker()
# obj.add(name,score)
# param_2 = obj.get()
