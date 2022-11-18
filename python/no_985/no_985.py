from typing import List


class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        cur_sum = sum([num for num in nums if num % 2 == 0])
        ret = []
        for q in queries:
            cur_val = nums[q[1]]
            nums[q[1]] += q[0]
            if cur_val % 2 == 1:
                if nums[q[1]] % 2 == 0:
                    cur_sum += nums[q[1]]
            else:
                if nums[q[1]] % 2 == 0:
                    cur_sum += q[0]
                else:
                    cur_sum -= cur_val
            ret.append(cur_sum)
        return ret
