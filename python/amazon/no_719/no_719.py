from typing import List


class Solution:
    def smallestDistancePair(self, nums: List[int], k: int) -> int:
        nums.sort()

        # sliding window & prefix sum
        def check(mid: int) -> bool:
            i, j = 0, 1
            smaller_pair_cnt = 0
            while i <= j:  # here we should allow i == j inorder not to exit too early
                while j < len(nums) and nums[j] - nums[i] <= mid:
                    j += 1
                smaller_pair_cnt += j - i - 1 if j > i else 0
                i += 1
            #  0 1 2 3 4 4 4 5 6 7
            #  × × × × √ √ √ √ √ √
            # here we want to find the left most possible answer
            # so the condition should be nums[j] - nums[i] <= mid (smaller_pair_cnt includes nums[j] - nums[i] == mid)
            # if we want to find 5, just change nums[j] - nums[i] <= mid to nums[j] - nums[i] < mid
            return smaller_pair_cnt >= k

        l, r = 0, max(nums) - min(nums)
        while l < r:
            mid = (l + r) // 2
            if check(mid):
                r = mid
            else:
                l = mid + 1

        return l
