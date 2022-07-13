package no_14

//14. Longest Common Prefix
//Write a function to find the longest common prefix string amongst an array of strings.
//
//If there is no common prefix, return an empty string "".

func longestCommonPrefix(strs []string) string {
	if strs == nil || len(strs) == 0 {
		return ""
	}
	prefix := ""
	i := 0
	for {
		if len(strs[0]) == i {
			return prefix
		}
		cur := strs[0][i]
		for j := 0; j < len(strs); j++ {
			if len(strs[j]) == i || cur != strs[j][i] {
				return prefix
			}
		}
		prefix += string(cur)
		i++
	}
}
