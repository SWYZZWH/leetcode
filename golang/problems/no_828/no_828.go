package no_828

// 828. Count Unique Characters of All Substrings of a Given String
//Let's define a function countUniqueChars(s) that returns the number of unique characters on s.
//
//For example, calling countUniqueChars(s) if s = "LEETCODE" then "L", "T", "C", "O", "D" are the unique characters since they appear only once in s, therefore countUniqueChars(s) = 5.
//Given a string s, return the sum of countUniqueChars(t) where t is a substring of s. The test cases are generated such that the answer fits in a 32-bit integer.
//
//Notice that some substrings can be repeated so in this case you have to count the repeated ones too.

//Constraints:
//
//1 <= s.length <= 105
//s consists of uppercase English letters only.

// the uniqueLetter for s[i:j] depends on the letter set of (i, j)
// use trick to achieve O(n)

func uniqueLetterString(s string) int {
	if len(s) == 0 {
		return 0
	}

	sumArray := make([]int, len(s))
	alphaMap := make(map[int32][]int)
	ret := 0
	for i := 0; i < len(s); i++ {
		if idx, ok := alphaMap[int32(s[i])]; ok {
			sumArray[i] += sumArray[i-1] + (i - 1 - idx[1]) - (idx[1] - idx[0] - 1)
			alphaMap[int32(s[i])] = []int{idx[1], i}
		} else {
			if i > 0 {
				sumArray[i] += sumArray[i-1] + i + 1
			} else {
				sumArray[i] = 1
			}
			alphaMap[int32(s[i])] = []int{-1, i}
		}
		ret += sumArray[i]
	}
	return ret
}

// for i in string, i new sets are met
// [0, i] [1, i], [2, i] ...
// sumArray[i] means the sum of these unique letters count
//
