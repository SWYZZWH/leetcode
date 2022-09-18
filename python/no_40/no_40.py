import collections
from typing import List


class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        freq = collections.Counter(candidates)
        cands = list(set(candidates))

        ret = []

        def dfs(prefix: List[int], prefix_sum: int, i: int):
            if prefix_sum == target:
                ret.append(prefix)
                return
            if i == len(cands):
                return
            cnt = min((target - prefix_sum) // cands[i], freq[cands[i]])
            for j in range(cnt + 1):
                dfs(prefix + [cands[i] for l in range(j)], prefix_sum + cands[i] * j, i + 1)

        dfs([], 0, 0)
        return ret
