# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:
def isBadVersion(version: int) -> bool:
    return True


class Solution:
    # classic binary search
    def firstBadVersion(self, n: int) -> int:
        l, r = 1, n + 1
        while l < r:
            mid = (l + r) // 2
            if not isBadVersion(mid):
                l = mid + 1
            else:
                r = mid
        return l
