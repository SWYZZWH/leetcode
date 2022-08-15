from typing import List


class Solution:
    # arr[i] shows up in (i + 1) * (n - i) times
    # and there is (i + 1) * (n - i) // 2 even subarrays and ((i + 1) * (n - i) + 1) // 2 are odd subarrays
    # number of odd subarray always equals to number of even subarrays
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        return sum([((i + 1) * (len(arr) - i) + 1) // 2 * arr[i] for i in range(len(arr))])