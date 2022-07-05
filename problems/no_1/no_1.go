package no_1

// [1. Two Sum](https://leetcode.com/problems/two-sum)
// 一次遍历，建好 val -> index 的 map，每次插入搜索 map
// multiple pairs version
func twoSum(nums []int, target int) []int {
	indexMap := map[int][]int{}
	for i, num := range nums {
		indexLst := indexMap[num]
		if indexLst == nil {
			indexMap[num] = []int{i}
		} else {
			indexMap[num] = append(indexLst, i)
		}
	}

	for i, num := range nums {
		indexLst, ok := indexMap[target-num]
		if !ok || indexLst == nil || len(indexLst) == 0 {
			continue
		}
		for _, j := range indexLst {
			if j <= i {
				continue
			}
			return []int{i, j}
		}
	}
	return nil
}

// one and only one pair
func twoSum2(nums []int, target int) []int {
	indexMap := make(map[int]int, len(nums))
	for i, num := range nums {
		idx, ok := indexMap[target-num]
		if ok {
			return []int{idx, i}
		}
		indexMap[num] = i
	}
	return nil
}
