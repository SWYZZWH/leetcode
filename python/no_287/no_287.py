from typing import List


class Solution:
    # the only possible solution is two pointers
    # try find cycle in nums:
    # 0: 1
    # 1: 3
    # 3: 2
    # 2: 4
    # 4: 2
    # and the start of a circle is 2 which is exactly the duplicated number

    # this is the only solution to reach O(1) space complexity, not change the input array and time complexity is O(n)
    # other O(n) ways can be:
    # mark number visited as - num
    # continuously move number to its position until find the duplicated number
    # use a set to remember visited
    def findDuplicate(self, nums: List[int]) -> int:
        i, j = 0, 0
        while True:
            i = nums[i]
            j = nums[nums[j]]
            if i == j:
                break

        k = 0
        while k != i:
            k = nums[k]
            i = nums[i]

        return k
