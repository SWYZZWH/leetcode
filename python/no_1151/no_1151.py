from typing import List


class Solution:
    # sliding window
    # find a interval that length equals 1 and with minimum zeroes
    def minSwaps(self, data: List[int]) -> int:
        ones = data.count(1)
        ret = cur = data[:ones].count(1)
        for i in range(ones, len(data)):
            cur -= data[i - ones] == 1
            cur += data[i] == 1
            ret = max(ret, cur)
        return ones - ret

