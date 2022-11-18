class Solution:
    def shoppingOffers(self, prices: List[int], specials: List[List[int]], needs: List[int]) -> int:
        @functools.cache
        def dp(cur_needs, cur_cost: int) -> int:
            if all(cur_needs[i] == 0 for i in range(len(cur_needs))):
                return cur_cost
            res = sum(cur_needs[i] * prices[i] for i in range(len(cur_needs))) + cur_cost
            for special in specials:
                new_needs = list(cur_needs)
                for i in range(len(special) - 1):
                    new_needs[i] = cur_needs[i] - special[i]
                if any(new_needs[i] < 0 for i in range(len(new_needs))):
                    continue
                res = min(res, dp(tuple(new_needs), cur_cost + special[-1]))

            return res

        return dp(tuple(needs), 0)
