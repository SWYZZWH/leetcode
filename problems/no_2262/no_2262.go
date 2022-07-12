package no_2262

//2262. Total Appeal of A String
//The appeal of a string is the number of distinct characters found in the string.
//
//For example, the appeal of "abbca" is 3 because it has 3 distinct characters: 'a', 'b', and 'c'.
//Given a string s, return the total appeal of all of its substrings.
//
//A substring is a contiguous sequence of characters within a string.

// Constraints:
//
//1 <= s.length <= 105
//s consists of lowercase English letters.

// appeal[i, j] means appeal for s[i,j]
// letterSet[i, j] = {c1, c2, ...}
// appealSum[i] = sum(appeal[0, i], appeal[1, i], ... , appeal[i,i])
// appealSum[i + 1] = sum(appeal[0, i + 1], appeal[1, i + 1], ... , appeal[i,i + 1] + appeal[i + 1, i + 1])
// = sum(appeal[0, i] + s[i+1] in letterSet[0, i] ? 0 : 1, appeal[1, i] + s[i+1] in letterSet[1, i] ? 0 : 1, ... , appeal[i,i] + s[i+1] in letterSet[i, i] ? 0 : 1, 1)
// = sum(appealSum[i], 1,  s[i+1] in letterSet[0, i] ? 0 : 1, s[i + 1] in letterSet[1, i] ? 0 : 1,..., s[i+1] in letterSet[i, i])
// notice that if s[i+1] is in letterSet[j, i], then it must be in letterSet[j - 1, i], letterSet[j - 2, i], ..., letterSet[0, i]
// we only have to maintain the last occurrence of each letter, for example, last[i][s[i+1]] = k
// then we have: s[i+1] is in letterSet[k, i], letterSet[k - 1, i], letterSet[k - 2, i], ... , letterSet[0, i] and
//
//	s[i+1] is not in letterSet[k+1, i], letterSet[k+2, i], letterSet[k+3, i], ... , letterSet[i, i]
//
// so appealSum[i + 1]= appealSum[i] + i - k (if can't find last occurrence, k = -1)
func appealSum(s string) int {
	lastOccurrence := make(map[int32]int, 128)

	ret := int64(0)
	sum := make([]int64, len(s))
	for i, c := range s {
		if i == 0 {
			sum[i] = 1
		} else {
			if idx, ok := lastOccurrence[c]; ok {
				sum[i] = sum[i-1] + int64(i-idx)
			} else {
				sum[i] = sum[i-1] + int64(1+i)
			}
		}

		lastOccurrence[c] = i
		ret += sum[i]
	}

	return int(ret)
}
