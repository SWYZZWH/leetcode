from typing import List


class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        m = max(nums)
        cnt = [0 for i in range(m + 1)]
        for num in nums:
            cnt[num] += 1

        previous = 0
        for i in range(m + 1):
            cur = cnt[i]
            cnt[i] = previous
            previous += cur

        ret = []
        for num in nums:
            ret.append(cnt[num])

        return ret
