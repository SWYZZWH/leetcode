package no_243

import "math"

//243. Shortest Word Distance
//Given an array of strings wordsDict and two different strings that already exist in the array word1 and word2, return the shortest distance between these two words in the list.

//Constraints:
//
//1 <= wordsDict.length <= 3 * 104
//1 <= wordsDict[i].length <= 10
//wordsDict[i] consists of lowercase English letters.
//word1 and word2 are in wordsDict.
//word1 != word2

// word can be duplicated in the wordsDict
// map[string][]int, if we got two list, compare each element in two lists, worst O(n ^ 2), best O(n)
// when we compare the elements, use double pointers, we can achieve O(n) complexity
//func shortestDistance(wordsDict []string, word1 string, word2 string) int {
//	dict := map[string][]int{}
//	for i, s := range wordsDict {
//		if dict[s] == nil {
//			dict[s] = []int{i}
//		} else {
//			dict[s] = append(dict[s], i)
//		}
//	}
//
//	idxLst1, idxLst2 := dict[word1], dict[word2]
//	dst := math.MaxInt
//	for i, j := 0, 0; i < len(idxLst1) && j < len(idxLst2); {
//		dst = min(dst, dist(idxLst1[i], idxLst2[j]))
//		if idxLst1[i] < idxLst2[j] {
//			i++
//		} else {
//			j++
//		}
//	}
//	return dst
//}

func dist(a, b int) int {
	if a > b {
		return a - b
	}
	return b - a
}

func min(a, b int) int {
	if a < b {
		return a
	}
	return b
}

// actually the best way is not to build index map
func shortestDistance(wordsDict []string, word1 string, word2 string) int {
	idx1, idx2 := -1, -1
	ret := math.MaxInt
	for i, s := range wordsDict {
		if s == word1 {
			idx1 = i
			if idx2 != -1 {
				ret = min(ret, dist(idx1, idx2))
			}
		} else if s == word2 {
			idx2 = i
			if idx1 != -1 {
				ret = min(ret, dist(idx1, idx2))
			}
		}
	}
	return ret
}
