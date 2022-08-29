import collections
from typing import List


class Solution:
    # back-tracking
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        d = collections.Counter(nums)
        ret = []
        key_list = list(d.keys())

        def dfs(i: int, prefix: List[int], ret: List[List[int]]):
            if i == len(key_list):
                ret.append(prefix)
                return

            for j in range(d[key_list[i]] + 1):
                dfs(i + 1, prefix + [key_list[i] for l in range(j)], ret)

        dfs(0, [], ret)

        return ret

    # cascading
    # sort first, instead of simply adding the current element
    # we could put one, two, ... , count(nums[i]) element to every subset before

    # 
