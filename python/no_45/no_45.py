class Solution:
    # greedy
    # maintain a left board and a right border
    def jump(self, nums: List[int]) -> int:
        left, right = 0, 0
        steps = 0
        for i, num in enumerate(nums):
            if i > left:
                left = right
                steps += 1
            right = max(right, i + nums[i])
            if right >= len(nums) - 1:
                return steps + 1 if left < len(nums) - 1 else steps  # opt 1, early returnw

        return steps