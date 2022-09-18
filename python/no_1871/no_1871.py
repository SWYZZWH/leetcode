import collections


class Solution:
    # simple dp will TLE
    # one pass solution, maintain left and right border
    # looks like simple BFS
    # more like sliding window, we need to check [i - maxJump, i - minJump], and this is a sliding window when comes to i - 1
    # we maintain the True count in this window, if this count equals 0, then it can not be reached
    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:
        if s[-1] == "1" or s[0] == "1":
            return False

        q = collections.deque([0])
        cur_r = 0
        while q:
            idx = q.popleft()
            for i in range(max(cur_r, idx + minJump), idx + maxJump + 1):
                if i >= len(s):
                    return False
                if s[i] == "1":
                    continue
                if i == len(s) - 1:
                    return True
                q.append(i)
            cur_r = idx + maxJump + 1

        return False
