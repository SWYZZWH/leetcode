from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        limit = 1 << n
        i = 0
        ret = []
        while i < limit:
            cur = []
            for j in range(n):
                if i & (1 << j):
                    cur.append(nums[j])
            ret.append(cur)
            i += 1

        return ret


# cascading
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        # cascading: like BFS
        ret = [[], [nums[0]]]

        for i in range(1, len(nums)):
            ret += [arr + [nums[i]] for arr in ret]

        return ret

# back-tracing:
# how to visit every possible solution
# divide the problem into sub problem:
#