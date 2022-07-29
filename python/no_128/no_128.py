from typing import List


class Solution:
    class UnionFind:
        def __init__(self, n):
            self.uf = [[i, 1] for i in range(n)]

        # j -> i
        def union(self, i, j) -> int:
            # note: i, j not in the
            idx_1, cnt_1 = self.find(i)[0], self.find(i)[1]
            idx_2, cnt_2 = self.find(j)[0], self.find(j)[1]
            if idx_1 == idx_2:
                return self.uf[idx_2][1]
            self.uf[idx_1] = [idx_2, cnt_1]
            self.uf[idx_2][1] += cnt_1
            return self.uf[idx_2][1]

        def find(self, i) -> List[int]:
            if self.uf[i][0] == i:
                return self.uf[i]
            pp = self.find(self.uf[i][0])
            self.uf[i][0] = pp[0]
            return pp

    def longestConsecutive(self, nums: List[int]) -> int:
        nums = list(set(nums))  # remove duplicated element
        if len(nums) == 0:
            return 0
        uf = self.UnionFind(len(nums))
        d = {}
        ret = 1
        for i in range(len(nums)):
            d[nums[i]] = i
            if nums[i] - 1 in d:
                ret = max(ret, uf.union(i, d[nums[i] - 1]))
            if nums[i] + 1 in d:
                ret = max(ret, uf.union(i, d[nums[i] + 1]))
        return ret


# this solution is clever
class Solution:
    def longestConsecutive(self, nums):
        longest_streak = 0
        num_set = set(nums)

        for num in num_set:
            if num - 1 not in num_set:
                current_num = num
                current_streak = 1

                while current_num + 1 in num_set:
                    current_num += 1
                    current_streak += 1

                longest_streak = max(longest_streak, current_streak)

        return longest_streak
