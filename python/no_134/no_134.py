# 134. Gas Station
# There are n gas stations along a circular route, where the amount of gas at the ith station is gas[i].
#
# You have a car with an unlimited gas tank and it costs cost[i] of gas to travel from the ith station to its next (i + 1)th station. You begin the journey with an empty tank at one of the gas stations.
#
# Given two integer arrays gas and cost, return the starting gas station's index if you can travel around the circuit once in the clockwise direction, otherwise return -1. If there exists a solution, it is guaranteed to be unique

from typing import List


class Solution:
    # find from back to the start
    # calculate the gain = gas - cost
    # sum = 0
    # fori(reverse) sum += cost
    #   if gain[i] > 0: sum += cost ; start = i ; sum = 0;
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        n, sum, start = len(gas), 0, -1
        gain = [gas[i] - cost[i] for i in range(n)]
        res = 0
        # optimize to finish in one pass
        for i in reversed(range(n)):
            sum += gain[i]
            if sum >= 0:
                start = i
                res += sum
                sum = 0
            i -= 1

        if sum + res < 0:
            return -1

        return start
