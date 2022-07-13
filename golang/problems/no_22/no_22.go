package no_22

import "strings"

//22. Generate Parentheses
//Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.
// 1 <= n <= 8

var cache map[int][]string

// generate recursively
func generateParenthesis(n int) []string {
	if cache == nil {
		cache = map[int][]string{}
	}

	if ret, ok := cache[n]; ok {
		return ret
	}

	if n == 0 {
		if _, ok := cache[n]; !ok {
			cache[n] = nil
		}
		return cache[n]
	}
	if n == 1 {
		if _, ok := cache[n]; !ok {
			cache[n] = []string{"()"}
		}
		return cache[n]
	}
	if n == 2 {
		if _, ok := cache[n]; !ok {
			cache[n] = []string{"(())", "()()"}
		}
		return cache[n]
	}

	ret := []string{}
	s := map[string]bool{}
	for i := 1; i < n; i++ {
		j := n - i
		pairs1, pairs2 := generateParenthesis(i), generateParenthesis(j)
		for k := 0; k < len(pairs1); k++ {
			for l := 0; l < len(pairs2); l++ {
				newStr := strings.Join([]string{pairs1[k], pairs2[l]}, "")
				if _, ok := s[newStr]; !ok {
					s[newStr] = true
				} else {
					continue
				}
				ret = append(ret, newStr)
			}
		}
	}

	for _, s2 := range generateParenthesis(n - 1) {
		newStr := strings.Join([]string{"(", s2, ")"}, "")
		if _, ok := s[newStr]; !ok {
			s[newStr] = true
		} else {
			continue
		}
		ret = append(ret, newStr)
	}

	if _, ok := cache[n]; !ok {
		cache[n] = ret
	}
	return cache[n]
}
