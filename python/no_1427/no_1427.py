from typing import List


# class Solution:
    # def stringShift(self, s: str, shift: List[List[int]]) -> str:
    #     amount = 0
    #     for sft in shift:
    #         if sft[0] == 0:
    #             amount -= sft[1]
    #         else:
    #             amount += sft[1]
    #     amount %= len(s)
    #     # now shift right by amount
    #     if amount == 0:
    #         return s
    #     return s[len(s) - amount:] + s[:len(s) - amount] if amount > 0 else s[(-amount) + 1:] + s[:(-amount) + 1]

# space complexity is O(1)
# however, we actually modify the input array
class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        n = len(nums)
        for i in range(n):
            num = nums[i]
            if nums[i] < 0:
                num = -nums[i]
            if nums[num - 1] > 0:
                nums[num - 1] = - nums[num - 1]

        ret = []
        for i in range(n):
            if nums[i] > 0:
                ret.append(i + 1)
        return ret
