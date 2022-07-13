package no_5

// Given a string s, return the longest palindromic substring in s.

func max(a, b int) int {
	if a > b {
		return a
	}
	return b
}

// use 2d DP to achieve O(n^2)
// other method could be finding 2n-1 corners and expand or manacher

func longestPalindrome(s string) string {
	dp := make([]bool, len(s))
	ret := 0
	left, right := 0, 0
	for i := 0; i < len(s); i++ {
		dp[i] = true
		ret = 1
		left, right = 0, 1
	}
	for i := 0; i < len(s); i++ {
		for j := 0; j < i; j++ {
			if s[i] == s[j] {
				if i == j || i-j == 1 || dp[j+1] {
					dp[j] = true
					if i-j+1 > ret {
						ret = max(ret, i-j+1)
						left, right = j, i+1
					}
				} else {
					dp[j] = false
				}
			} else {
				dp[j] = false
			}
		}
	}
	return s[left:right]
}
