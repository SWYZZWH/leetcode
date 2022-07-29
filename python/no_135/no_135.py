# There are n children standing in a line. Each child is assigned a rating value given in the integer array ratings.
#
# You are giving candies to these children subjected to the following requirements:
#
# Each child must have at least one candy.
# Children with a higher rating get more candies than their neighbors.
# Return the minimum number of candies you need to have to distribute the candies to the children.

# Constraints:
#
# n == ratings.length
# 1 <= n <= 2 * 104
# 0 <= ratings[i] <= 2 * 104
import math
from typing import List


class Solution:
    # use binary search:
    # find minimal value template
    # however, with a certain sum of candies, check() is hard to write

    # strategy:
    # r for ratings, c for candies array
    # from left:
    #   if r[0] <= r[1], then r[0] = 1
    #   else r[0] = r[1] + 1
    # for element in the mid:
    #   r[i-1]: depends on right(will never depend on left) or a certain val
    #   if r[i] <= r[i-1] and r[i] <= r[i+1]: then c[i] = 1
    #   elif r[i] > r[i-1] and r[i] <= r[i+1]: then c[i] = c[i-1] + 1 # c[i-1] + 1 is a decided number
    #   elif r[i] <= r[i-1] and r[i] > r[i+1]: then c[i] = c[i+1] + 1
    #   else: r[i] > r[i-1] and r[i] > r[i+1]: then c[i] = max(c[i+1] + 1, c[i-1] + 1) # c[i-1] + 1 is a decided number
    #   actually, we can modify the ratings as [+math.inf, ratings , +math.inf]

    def candy(self, ratings: List[int]) -> int:
        # False for not ready
        candies = [(0, True)] + [(1, False) for i in range(len(ratings))] + [(0, True)]
        ratings = [-math.inf] + ratings[:] + [math.inf]

        for i in range(1, len(candies) - 1):
            if ratings[i] <= ratings[i + 1]:
                if ratings[i] > ratings[i - 1]:
                    candies[i] = (candies[i - 1][0] + 1, True)
                else:
                    candies[i] = (1, True)

        for i in reversed(range(1, len(candies) - 1)):
            if not candies[i][1]:
                if ratings[i] <= ratings[i - 1]:
                    candies[i] = (candies[i + 1][0] + 1, True)
                else:
                    candies[i] = (max(candies[i - 1][0], candies[i + 1][0]) + 1, True)

        return sum([c[0] for c in candies])
