package no_2062

// 2062. Count Vowel Substrings of a String
//A substring is a contiguous (non-empty) sequence of characters within a string.
//
//A vowel substring is a substring that only consists of vowels ('a', 'e', 'i', 'o', and 'u') and has all five vowels present in it.
//
//Given a string word, return the number of vowel substrings in word.

//1 <= word.length <= 100
//word consists of lowercase English letters only.

// distance means count of substrings
func countVowelSubstrings(word string) int {
	if len(word) < 5 {
		return 0
	}

	ret := 0
	vowels := make(map[int32]int)

	for i, j := 0, 0; j < len(word); j++ {
		if !isVowel(int(word[j])) {
			vowels = make(map[int32]int)
			i = j + 1
			continue
		}

		vowels[int32(word[j])]++
		if !checkAll(vowels) {
			continue
		}

		// move k
		k := i
		for checkAll(vowels) {
			vowels[int32(word[k])]--
			k++
		}

		for l := i; l < k; l++ {
			vowels[int32(word[l])]++
		}

		ret += k - i
	}
	return ret
}

func checkAll(vowels map[int32]int) bool {
	if vowels['a'] > 0 && vowels['e'] > 0 && vowels['i'] > 0 && vowels['o'] > 0 && vowels['u'] > 0 {
		return true
	}
	return false
}

func isVowel(c int) bool {
	return c == 'a' || c == 'e' || c == 'i' || c == 'o' || c == 'u'
}
