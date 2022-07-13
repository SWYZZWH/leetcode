package no_3

// Longest Substring Without Repeating Characters
// Given a string s, find the length of the longest substring(continuous) without repeating characters.

func max(a, b int) int {
	if a > b {
		return a
	}
	return b
}

// alphabet map
func lengthOfLongestSubstring(s string) int {
	if len(s) == 0 {
		return 0
	}
	mp := make(map[int32]int)
	maxLen := 0
	left := 0
	for i, c := range s {
		if idx, ok := mp[c]; ok && idx >= left {
			maxLen = max(maxLen, i-left)
			left = idx + 1
		}
		mp[c] = i
	}
	return max(maxLen, len(s)-left)
}
