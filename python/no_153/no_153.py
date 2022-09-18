class Solution:
    def findMin(self, nums: List[int]) -> int:
        if len(nums) == 1 or nums[0] < nums[-1]:
            return nums[0]

        if len(nums) == 2:
            return min(nums)

        l, r = 0, len(nums)
        while l < r:
            mid = (l + r) // 2
            if (mid - 1 >= 0 and nums[mid] < nums[mid - 1]) and (mid + 1 < len(nums) and nums[mid] < nums[mid + 1]):
                return nums[mid]

            if nums[mid] >= nums[0]:
                l = mid + 1
            else:
                r = mid

        return nums[l]