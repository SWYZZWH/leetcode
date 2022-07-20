# 2197. Replace Non-Coprime Numbers in Array

# You are given an array of integers nums. Perform the following steps:
#
# Find any two adjacent numbers in nums that are non-coprime.
# If no such numbers are found, stop the process.
# Otherwise, delete the two numbers and replace them with their LCM (Least Common Multiple).
# Repeat this process as long as you keep finding two adjacent non-coprime numbers.
# Return the final modified array. It can be shown that replacing adjacent non-coprime numbers in any arbitrary order will lead to the same result.
#
# The test cases are generated such that the values in the final array are less than or equal to 108.
#
# Two values x and y are non-coprime if GCD(x, y) > 1 where GCD(x, y) is the Greatest Common Divisor of x and y.
import math
from typing import List


class Solution:
    def replaceNonCoprimes(self, nums: List[int]) -> List[int]:
        stk = []
        for i in range(len(nums)):
            if len(stk) == 0 or math.gcd(nums[i], stk[-1]) == 1:
                stk.append(nums[i])
                continue

            stk[-1] = math.lcm(stk[-1], nums[i])
            while len(stk) > 1 and math.gcd(stk[-2], stk[-1]) != 1:
                top = stk.pop()
                stk[-1] = math.lcm(stk[-1], top)

        return stk
