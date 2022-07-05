package no_680

// 680. Valid Palindrome II

// naive idea: try to delete every possible position
//
//	func validPalindrome(s string) bool {
//		for i := 0; i < len(s); i++ {
//			if isPalindrome(s[:i] + s[i+1:]) {
//				return true
//			}
//		}
//		return false
//	}
func isPalindrome(s string) bool {
	if len(s) == 0 {
		return true
	}

	for i := 0; i < len(s)/2; i++ {
		j := len(s) - 1 - i
		if s[i] != s[j] {
			return false
		}
	}

	return true
}

// better: go and find the position
// notice: when find the wrong position, still need to check if there is another wrong position
func validPalindrome(s string) bool {
	for i := 0; i < len(s)/2; i++ {
		j := len(s) - 1 - i
		if s[i] != s[j] {
			if s[i] == s[j-1] && isPalindrome(s[i:j]) {
				return true
			}
			if s[j] == s[i+1] && isPalindrome(s[i+1:j+1]) {
				return true
			}
			return false
		}
	}
	return true
}
