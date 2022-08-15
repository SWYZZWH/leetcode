class Solution:
    # sliding window
    def longestOnes(self, nums: List[int], k: int) -> int:
        # no need to compress
        #         ones = []
        #         zeroes = []
        #         cur = nums[0]
        #         idx = 0
        #         for i in range(1, len(nums) + 1):
        #             if i == len(nums) + 1:
        #                 if cur == 1:
        #                     ones.append(i - idx)
        #                 else:
        #                     zeroes.append(i - idx)
        #                 continue
        #             if nums[i] != cur:
        #                 if cur == 1:
        #                     ones.append(i - idx)
        #                 else:
        #                     zeroes.append(i - idx)
        #                 cur = nums[i]
        #                 idx = i

        #         ret = 0
        #         if len(ones) == 0:
        #             return ret

        #         res = k
        #         cur_prefix = ones[0]
        #         # costs = []
        #         i, j = 0, 0
        #         while j != len(zeroes):
        #             if res >= zeroes[j]:
        #                 res -= zeroes[j]
        #                 cur_prefix += ones[i]

        i, j = 0, 0
        res = k
        ret = 0
        while j != len(nums):
            if nums[j] == 1:
                j += 1
                ret = max(ret, j - i)
                continue
            if res == 0:
                # no need to mark
                # while nums[i] != 2:
                while nums[i] != 0:
                    i += 1
                i += 1
            else:
                res -= 1
            j += 1
            ret = max(ret, j - i)

        return ret
