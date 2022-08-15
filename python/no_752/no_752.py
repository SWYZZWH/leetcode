import collections
from typing import List


class Solution:
    # BFS problem!
    # maintain the minimum distance dict for each possible lock state
    # d[target] = 0
    # change one digit to every possbile state
    def openLock(self, deadends: List[str], target: str) -> int:
        d = {}
        q = collections.deque()

        q.append(("0000", 0))
        lst = [str(i) for i in range(10)]
        deadends = set(deadends)

        if "0000" in deadends:
            return -1
        while q:
            state = q.popleft()
            if state[0] not in d:
                d[state[0]] = state[1]
                # q.append()

            if state[0] == target:
                return state[1]

            # try change one digit
            for i in range(len(target)):
                cur = ord(state[0][i]) - ord("0")
                # clock-wise
                new_clock = state[0][:i] + lst[(cur + 1) % 10] + state[0][i + 1:]
                if new_clock not in deadends and new_clock not in d:
                    d[new_clock] = state[1] + 1
                    q.append((new_clock, state[1] + 1))

                # reversed clock-wise
                new_clock = state[0][:i] + lst[(cur - 1) % 10] + state[0][i + 1:]
                if new_clock not in deadends and new_clock not in d:
                    d[new_clock] = state[1] + 1
                    q.append((new_clock, state[1] + 1))

                # for j in range(1, 10):
                #     left += 1
                #     new_clock = state[0][:i] + lst[(cur + j) % 10] + state[0][i + 1:]

                # reversed clock-wise
                # right = 0
                # for j in range(1, 10):
                #     right += 1
                #     new_clock = state[0][:i] + lst[(cur - j) % 10] + state[0][i + 1:]
                #     if new_clock in deadends:
                #         break
                #     if new_clock not in d or d[new_clock] > state[1] + 1 + right:
                #         d[new_clock] = state[1] + 1 + right
                #         q.append((new_clock, state[1] + 1 + right))
        return -1
