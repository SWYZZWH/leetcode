import math


class Solution:
    # TLE in python
    # works well in Golang
    def countPrimes(self, n: int) -> int:
        arr = [0, 0] + [1 for i in range(n - 2)]
        for i in range(2, min(math.ceil(math.sqrt(n)), n + 1)):
            if not arr[i]:
                continue
            j = 2
            while i * j < n:
                arr[i * j] = 0
                j += 1
        return sum(arr)
