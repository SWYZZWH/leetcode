# 2305. Fair Distribution of Cookies
# Constraints:
#
# 2 <= cookies.length <= 8
# 1 <= cookies[i] <= 105
# 2 <= k <= cookies.length

# You are given an integer array cookies, where cookies[i] denotes the number of cookies in the ith bag. You are also given an integer k that denotes the number of children to distribute all the bags of cookies to. All the cookies in the same bag must go to the same child and cannot be split up.
#
# The unfairness of a distribution is defined as the maximum total cookies obtained by a single child in the distribution.
#
# Return the minimum unfairness of all distributions.
import math
from typing import List


class Solution:
    def num2array(self, num: int, m: int, k: int) -> List[int]:
        help = [0 for i in range(m)]
        i = 0
        while num != 0:
            help[i] = num % k
            i += 1
            num //= k
        return help

    def distributeCookies(self, cookies: List[int], k: int) -> int:
        # as the length of cookies and k is only 2 to 8, we could try every partition and get the min(max())
        m = len(cookies)
        if m == k:
            return max(cookies)
        min_max = 1_000_000_000
        for i in range(k ** len(cookies)):
            ret = [0 for i in range(k)]
            help = self.num2array(i, m, k)
            for j in range(m):
                ret[help[j]] += cookies[j]
            # print(ret, min_max)
            cur_max = max(ret)
            min_max = min(min_max, cur_max)
        return min_max
