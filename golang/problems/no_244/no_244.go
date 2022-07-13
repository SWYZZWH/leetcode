package no_244

import "math"

//244. Shortest Word Distance II

//Design a data structure that will be initialized with a string array, and then it should answer queries of the shortest distance between two different strings from the array.
//
//Implement the WordDistance class:
//
//WordDistance(String[] wordsDict) initializes the object with the strings array wordsDict.
//int shortest(String word1, String word2) returns the shortest distance between word1 and word2 in the array wordsDict.

// 1 <= wordsDict.length <= 3 * 104
// 1 <= wordsDict[i].length <= 10
// wordsDict[i] consists of lowercase English letters.
// word1 and word2 are in wordsDict.
// word1 != word2
// At most 5000 calls will be made to shortest.

// WordDistance can use cache to speed up
type WordDistance struct {
	cache map[string]map[string]int
	dict  map[string][]int
}

func Constructor(wordsDict []string) WordDistance {
	dict := map[string][]int{}
	for i, s := range wordsDict {
		if dict[s] == nil {
			dict[s] = []int{i}
		} else {
			dict[s] = append(dict[s], i)
		}
	}
	return WordDistance{
		cache: map[string]map[string]int{},
		dict:  dict,
	}
}

func (this *WordDistance) Shortest(word1 string, word2 string) int {
	if ca, ok := this.cache[word1]; ok {
		if dst, ok := ca[word2]; ok {
			return dst
		}
	}
	idxLst1, idxLst2 := this.dict[word1], this.dict[word2]
	dst := math.MaxInt
	for i, j := 0, 0; i < len(idxLst1) && j < len(idxLst2); {
		dst = min(dst, dist(idxLst1[i], idxLst2[j]))
		if idxLst1[i] < idxLst2[j] {
			i++
		} else {
			j++
		}
	}
	if _, ok := this.cache[word1]; ok {
		this.cache[word1][word2] = dst
	} else {
		this.cache[word1] = map[string]int{word2: dst}
	}
	return dst
}

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
