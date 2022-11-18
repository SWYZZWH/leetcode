class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        n = len(arr)
        if k >= n:
            return arr

        idx = bisect.bisect_right(arr, x)
        l, r = idx, idx - 1
        while r - l + 1 < k:
            if not 0 <= r + 1 < n:
                l -= 1
            elif not 0 <= l - 1 < n:
                r += 1
            else:
                if abs(arr[l - 1] - x) > abs(arr[r + 1] - x):
                    r += 1
                else:
                    l -= 1

        return arr[l: r + 1]

class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        # Initialize binary search bounds
        left = 0
        right = len(arr) - k

        # Binary search against the criteria described
        while left < right:
            mid = (left + right) // 2
            if x - arr[mid] > arr[mid + k] - x:
                left = mid + 1
            else:
                right = mid

        return arr[left:left + k]