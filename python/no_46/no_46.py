import itertools
from typing import List


class Solution:
    # implement next_permutation
    def permute(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ret = [perm for perm in itertools.permutations(nums)]

        return ret
