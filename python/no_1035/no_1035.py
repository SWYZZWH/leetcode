import collections
from typing import List


class Solution:
    # dp[i][j] equals the max lines we can connects for the first i elements of nums1 and j elements of nums2
    # if nums1[i - 1] == nums2[j - 1], then we simply draw this line, dp[i][j] = dp[i - 1][j - 1] + 1
    # else we find the last index of nums1[i - 1] in nums2[:i] (idx1) and nums2[j - 1] in nums1[:j] (idx2)
    # dp[i][j] = max(dp[i - 1][idx1 - 1], dp[idx2 - 1][j - 1])
    # also, we can simply give up the nums1[i - 1] and nums2[j - 1], in that case
    # dp[i][j] = max(dp[i][j], dp[i - 1][j - 1])

    # naive O(n^3) solution
    # O(n^2 log n) is possible
    # how about O(n^2) also possible, dict optimization

    # actually the same as longest common subsequence
    def maxUncrossedLines(self, nums1: List[int], nums2: List[int]) -> int:
        m, n = len(nums1), len(nums2)
        dp = [[0 for i in range(n + 1)] for j in range(m + 1)]

        last_occur_1 = collections.defaultdict(int)
        for i in range(1, m + 1):
            last_occur_2 = collections.defaultdict(int)
            for j in range(1, n + 1):
                if nums1[i - 1] == nums2[j - 1]:
                    dp[i][j] = max(dp[i][j], dp[i - 1][j - 1] + 1)

                idx1, idx2 = last_occur_2[nums1[i - 1]], last_occur_1[nums2[j - 1]]
                if idx1 != 0:
                    dp[i][j] = max(dp[i][j], dp[i - 1][idx1 - 1] + 1)

                if idx2 != 0:
                    dp[i][j] = max(dp[i][j], dp[idx2 - 1][j - 1] + 1)

                dp[i][j] = max(dp[i][j], dp[i - 1][j - 1])

                last_occur_2[nums2[j - 1]] = j
            last_occur_1[nums1[i - 1]] = i

        return dp[-1][-1]
