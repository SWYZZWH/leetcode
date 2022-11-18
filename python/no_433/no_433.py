import collections
from typing import List


class Solution:
    def minMutation(self, start: str, end: str, bank: List[str]) -> int:
        bank_set = set(bank)
        visited = {start}
        if end not in bank_set:
            return -1

        def is_similar(s1: str, s2: str) -> bool:
            if len(s1) != len(s2):
                return False
            diff = 0
            for i in range(len(s1)):
                if s1[i] != s2[i]:
                    diff += 1

            return diff == 1

        q = collections.deque([start])
        dist = 0
        while q:
            tmp = collections.deque()
            while q:
                e = q.popleft()
                for s in bank_set:
                    if s in visited:
                        continue
                    if is_similar(s, e):
                        if s == end:
                            return dist + 1
                        if is_similar(s, end):
                            return dist + 2
                        tmp.append(s)
                        visited.add(s)
            q = tmp
            dist += 1

        return -1