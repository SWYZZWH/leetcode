from typing import List


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        def k_smallest(a: List[int], b: List[int], k: int):
            if not a:
                return b[k]
            if not b:
                return a[k]

            mid1, mid2 = len(a) // 2, len(b) // 2
            if mid1 + mid2 < k:  # key
                if a[mid1] <= b[mid2]:
                    return k_smallest(a[mid1 + 1:], b, k - mid1 - 1)
                else:
                    return k_smallest(a, b[mid2 + 1:], k - mid2 - 1)
            else:
                if a[mid1] <= b[mid2]:
                    return k_smallest(a, b[:mid2], k)
                else:
                    return k_smallest(a[:mid1], b, k)

        m, n = len(nums1), len(nums2)
        if (m + n) % 2 == 1:
            return k_smallest(nums1, nums2, (m + n) // 2)
        return (k_smallest(nums1, nums2, (m + n) // 2) + k_smallest(nums1, nums2, (m + n) // 2 - 1)) / 2.
