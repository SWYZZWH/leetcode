package no_1152

import (
	"github.com/emirpasic/gods/trees/binaryheap"
	"strings"
)

// 1152. Analyze User Website Visit Pattern

// You are given two string arrays username and website and an integer array timestamp. All the given arrays are of the same length and the tuple [username[i], website[i], timestamp[i]] indicates that the user username[i] visited the website website[i] at time timestamp[i].
//
//A pattern is a list of three websites (not necessarily distinct).
//
//For example, ["home", "away", "love"], ["leetcode", "love", "leetcode"], and ["luffy", "luffy", "luffy"] are all patterns.
//The score of a pattern is the number of users that visited all the websites in the pattern in the same order they appeared in the pattern.
//
//For example, if the pattern is ["home", "away", "love"], the score is the number of users x such that x visited "home" then visited "away" and visited "love" after that.
//Similarly, if the pattern is ["leetcode", "love", "leetcode"], the score is the number of users x such that x visited "leetcode" then visited "love" and visited "leetcode" one more time after that.
//Also, if the pattern is ["luffy", "luffy", "luffy"], the score is the number of users x such that x visited "luffy" three different times at different timestamps.
//Return the pattern with the largest score. If there is more than one pattern with the same largest score, return the lexicographically smallest such pattern.

//Constraints:
//
//3 <= username.length <= 50
//1 <= username[i].length <= 10
//timestamp.length == username.length
//1 <= timestamp[i] <= 109
//website.length == username.length
//1 <= website[i].length <= 10
//username[i] and website[i] consist of lowercase English letters.
//It is guaranteed that there is at least one user who visited at least three websites.
//All the tuples [username[i], timestamp[i], website[i]] are unique.

// fucking tedious
// notice: every user only has one score for one pattern!

type VisitInfo struct {
	userName  string
	timestamp int
	website   string
}

func mostVisitedPattern(username []string, timestamp []int, website []string) []string {

	pq := binaryheap.NewWith(func(a, b interface{}) int {
		info1, info2 := a.(VisitInfo), b.(VisitInfo)
		return info1.timestamp - info2.timestamp
	})

	for i := 0; i < len(username); i++ {
		pq.Push(VisitInfo{
			userName:  username[i],
			timestamp: timestamp[i],
			website:   website[i],
		})
	}

	userInfo := map[string][]string{}
	for !pq.Empty() {
		v, _ := pq.Pop()
		info := v.(VisitInfo)
		if infos, ok := userInfo[info.userName]; !ok {
			userInfo[info.userName] = []string{info.website}
		} else {
			userInfo[info.userName] = append(infos, info.website)
		}
	}

	freq := map[string][]int{}
	maxFreq := 0
	maxKey := ""
	user := 0
	for _, infos := range userInfo {
		for i := 0; i < len(infos)-2; i++ {
			for j := i + 1; j < len(infos)-1; j++ {
				for k := j + 1; k < len(infos); k++ {
					key := strings.Join([]string{infos[i], infos[j], infos[k]}, "_")
					if _, ok := freq[key]; !ok {
						freq[key] = []int{1, user}
						if 1 >= maxFreq {
							if maxKey == "" {
								maxKey = key
							} else if 1 == maxFreq {
								maxKeySplit := strings.Split(maxKey, "_")
								s1, s2, s3 := maxKeySplit[0], maxKeySplit[1], maxKeySplit[2]
								if s1 > infos[i] || (s1 == infos[i] && s2 > infos[j]) || (s1 == infos[i] && s2 == infos[j] && s3 > infos[k]) {
									maxKey = key
								}
							} else {
								maxKey = key
							}
							maxFreq = 1
						}
					} else {
						f, ur := freq[key][0], freq[key][1]
						if ur == user {
							continue
						}
						freq[key] = []int{f + 1, user}
						if f+1 >= maxFreq {
							if maxKey == "" {
								maxKey = key
							} else if f+1 == maxFreq {
								maxKeySplit := strings.Split(maxKey, "_")
								s1, s2, s3 := maxKeySplit[0], maxKeySplit[1], maxKeySplit[2]
								if s1 > infos[i] || (s1 == infos[i] && s2 > infos[j]) || (s1 == infos[i] && s2 == infos[j] && s3 > infos[k]) {
									maxKey = key
								}
							} else {
								maxKey = key
							}
							maxFreq = f + 1
						}
					}
				}
			}
		}
		user++
	}

	return strings.Split(maxKey, "_")
}

//func mostVisitedPattern(username []string, timestamp []int, website []string) []string {
//	// sort the list based on user and time
//	order := make([]int, len(username))
//	for i := range order {
//		order[i] = i
//	}
//
//	sort.Slice(order, func(i,j int) bool {
//		if username[order[i]] == username[order[j]] {
//			return timestamp[order[i]] < timestamp[order[j]]
//		} else {
//			return username[order[i]]< username[order[j]]
//		}
//	})
//	threeSequence := make(map[string]int)
//	threeSequenceUser := make(map[string]string)
//	maxThree :=""
//	max := 0
//	for i:= 0; i < len(username); i++ {
//		currentUser := username[order[i]]
//		for j:= i+1; j < len(username) && currentUser == username[order[j]]; j++ {
//			for k := j+1; k < len(username)&&currentUser == username[order[k]]; k++ {
//				seq := website[order[i]]+":"+website[order[j]]+":"+website[order[k]]
//				if threeSequenceUser[seq] == currentUser {
//					continue
//				} else {
//					threeSequenceUser[seq] = currentUser
//				}
//
//				threeSequence[seq] = threeSequence[seq]+1
//				if threeSequence[seq] > max {
//					max = threeSequence[seq]
//					maxThree = seq
//				} else if threeSequence[seq] == max {
//					if seq < maxThree {
//						max = threeSequence[seq]
//						maxThree = seq
//					}
//				}
//			}
//
//
//		}
//	}
//	return strings.Split(maxThree, ":")
//}
