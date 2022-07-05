package no_4

import "math"

// 4. Median of Two Sorted Arrays

// findMedianSortedArrays
// hard due to border cases, however, adding imaginary numbers makes easier and cleaner
// [1, 2, 3] (N)-> [#, 1, #, 2, #, 3, #] (2 N + 1) always odd, notice that cut position is always N
// notice: when you cut an array in the middle: L = (N - 1) / 2 ; R = N / 2
// two arrays are divided individually as : L1 R1 L2 R2, we search for the position C1 C2 let:
// L1 >= R1 && L1 >= R2 && L2 >= R1 && L2 >= R2
// search this position through binary search to get O(log(m + n))
// always handle the shorter array directly, it will be much easier
func findMedianSortedArrays(nums1 []int, nums2 []int) float64 {
	m, n := len(nums1), len(nums2)
	if m < n {
		return findMedianSortedArrays(nums2, nums1)
	}

	lo, hi := 0, 2*n
	for true {
		mid2 := (lo + hi) / 2 // cut point 2
		mid1 := m + n - mid2  // cut point 1

		l1, r1 := math.MinInt, math.MaxInt
		l2, r2 := math.MinInt, math.MaxInt
		if mid1 != 0 {
			l1 = nums1[(mid1-1)/2]
		}
		if mid2 != 0 {
			l2 = nums2[(mid2-1)/2]
		}
		if mid1 != 2*m {
			r1 = nums1[mid1/2]
		}
		if mid2 != 2*n {
			r2 = nums2[mid2/2]
		}

		if l1 > r2 {
			lo = mid2 + 1
		} else if l2 > r1 {
			hi = mid2 - 1
		} else {
			return float64(max(l1, l2)+min(r1, r2)) / 2.0
		}
	}
	return -1
}

func min(a, b int) int {
	if a < b {
		return a
	}
	return b
}

func max(a, b int) int {
	if a > b {
		return a
	}
	return b
}
