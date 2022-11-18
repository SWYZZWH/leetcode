# sorted dict
import sortedcontainers


class TimeMap:

    def __init__(self):
        self.c = sortedcontainers.SortedSet()
        self.c.add()
        self.m = sortedcontainers.SortedDict()

    def set(self, key: str, value: str, timestamp: int) -> None:


    def get(self, key: str, timestamp: int) -> str: