import math
from typing import List


class Solution:
    # this solution is precise
    # def getFactors(self, n):
    #     def factor(n, i, combi, combis):
    #         while i * i <= n:
    #             if n % i == 0:
    #                 combis += combi + [i, n/i],
    #                 factor(n/i, i, combi+[i], combis)
    #             i += 1
    #         return combis
    #     return factor(n, 2, [], [])

    # simple idea is get all prime factors and allocate factors to each combination, however it's too complicated
    # the only solution is do it recursively to avoid the complexity
    def getFactors(self, n: int) -> List[List[int]]:
        #         primes = {2: True}
        #         def isPrime(n: int) -> bool:
        #             if n in primes:
        #                 return primes[n]
        #             for i in range(2, math.ceil(math.sqrt(n))):
        #                 if n % i == 0:
        #                     primes[n] = True
        #                     return True
        #                 primes[n] = False
        #                 return False

        # time exceeding if without cache
        cache = {2: [[2]], 3: [[3]]}

        def dfs(n: int) -> List[List[int]]:
            if n in cache:
                return cache[n]

            ret = []
            for i in range(2, math.floor(math.sqrt(n)) + 1):

                if n != 2 and n % i == 0:
                    sub_combinations = dfs(n // i)
                    for sub in sub_combinations:
                        # remove duplicated
                        if i <= min(sub):
                            ret.append([i] + sub)
            ret.append([n])
            cache[n] = ret
            return ret

        return [c for c in dfs(n) if len(c) > 1]
