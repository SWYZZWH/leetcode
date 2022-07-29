import math
from typing import List


class Solution:
    # debt[i] means the money owed by each person
    # if i owes 10 dollars, try each person in [i+1:], which debt is negative, let i owes him money
    def dfs(self, debt: List[int], i: int) -> int:
        while i < 12 and debt[i] == 0:
            i += 1
        if i == 12:
            return 0

        rest_cost = 9999
        for j in range(i + 1, 12):
            if debt[j] * debt[i] < 0:
                debt[j] += debt[i]
                rest_cost = min(rest_cost, self.dfs(debt, i + 1) + 1)
                debt[j] -= debt[i]
        return rest_cost

    def minTransfers(self, transactions: List[List[int]]) -> int:
        debt = [0 for i in range(12)]
        for tran in transactions:
            debt[tran[0]] -= tran[2]
            debt[tran[1]] += tran[2]

        return self.dfs(debt, 0)
