package no_17

// 17. Letter Combinations of a Phone Number

//Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent. Return the answer in any order.
//
//A mapping of digits to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.

// simple dfs
func letterCombinations(digits string) []string {
	if len(digits) == 0 {
		return nil
	}
	return dfs(digits, "")
}

func dfs(digits, prefix string) []string {
	if len(prefix) == len(digits) {
		return []string{prefix}
	}

	cur := len(prefix)
	ret := []string{}
	if digits[cur] == '2' {
		ret = append(ret, dfs(digits, prefix+"a")...)
		ret = append(ret, dfs(digits, prefix+"b")...)
		ret = append(ret, dfs(digits, prefix+"c")...)
	} else if digits[cur] == '3' {
		ret = append(ret, dfs(digits, prefix+"d")...)
		ret = append(ret, dfs(digits, prefix+"e")...)
		ret = append(ret, dfs(digits, prefix+"f")...)
	} else if digits[cur] == '4' {
		ret = append(ret, dfs(digits, prefix+"g")...)
		ret = append(ret, dfs(digits, prefix+"h")...)
		ret = append(ret, dfs(digits, prefix+"i")...)
	} else if digits[cur] == '5' {
		ret = append(ret, dfs(digits, prefix+"j")...)
		ret = append(ret, dfs(digits, prefix+"k")...)
		ret = append(ret, dfs(digits, prefix+"l")...)
	} else if digits[cur] == '6' {
		ret = append(ret, dfs(digits, prefix+"m")...)
		ret = append(ret, dfs(digits, prefix+"n")...)
		ret = append(ret, dfs(digits, prefix+"o")...)
	} else if digits[cur] == '7' {
		ret = append(ret, dfs(digits, prefix+"p")...)
		ret = append(ret, dfs(digits, prefix+"q")...)
		ret = append(ret, dfs(digits, prefix+"r")...)
		ret = append(ret, dfs(digits, prefix+"s")...)
	} else if digits[cur] == '8' {
		ret = append(ret, dfs(digits, prefix+"t")...)
		ret = append(ret, dfs(digits, prefix+"u")...)
		ret = append(ret, dfs(digits, prefix+"v")...)
	} else if digits[cur] == '9' {
		ret = append(ret, dfs(digits, prefix+"w")...)
		ret = append(ret, dfs(digits, prefix+"x")...)
		ret = append(ret, dfs(digits, prefix+"y")...)
		ret = append(ret, dfs(digits, prefix+"z")...)
	}
	return ret
}
