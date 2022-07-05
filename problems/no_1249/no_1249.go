package no_1249

import (
	"awesomeProject/utils/stack"
)

//[146. LRU Cache](https://leetcode.com/problems/lru-cache)
//字符可以忽略
//对偶括号 要用栈

// classic 2D dp
//func minRemoveToMakeValid(s string) string {
//	if len(s) == 0 {
//		return s
//	}
//	minRemoveToMakeValid(s)
//}

func isParen(s string) bool {
	if s == "(" || s == ")" {
		return true
	} else {
		return false
	}
}

// try recursive algo, but failed
//
//	func minRemoveToMakeValid(s string) string {
//		if len(s) == 0 {
//			return s
//		}
//
//		if len(s) == 1 {
//			if isParen(s) {
//				return ""
//			} else {
//				return s
//			}
//		}
//
//		if s[0:1] == "(" && s[len(s)-1:] == ")" {
//			return "(" + minRemoveToMakeValid(s[1:len(s)-1]) + ")"
//		}
//
//		if isParen(s[0:1]) && isParen(s[len(s)-1:]) {
//			left := minRemoveToMakeValid(s[0:len(s)-1])
//			right := minRemoveToMakeValid(s[1:])
//			if len(left) > len(right) {
//				return left
//			} else {
//				return right
//			}
//		}
//
//		left, right := "", ""
//		if !isParen(s[0:1]) {
//			left = s[0:1] + minRemoveToMakeValid(s[1:])
//		}
//		if !isParen(s[len(s)-1:]) {
//			right = minRemoveToMakeValid(s[:len(s)-1]) + s[len(s)-1:]
//		}
//		if len(left) > len(right) {
//			return left
//		} else {
//			return right
//		}
//	}
func min(a, b int) int {
	if a < b {
		return a
	}
	return b
}

// try dp, still fail

//func minRemoveToMakeValid(s string) string {
//	pars := []int{}
//	for i, c := range s {
//		if c == '(' || c == ')' {
//			pars = append(pars, i)
//		}
//	}
//
//	dp := [][]int{}
//	for i := 0; i < len(pars); i++ {
//		newRow := []int{}
//		for j := 0; j < len(pars); j++ {
//			newRow = append(newRow, 0)
//		}
//		dp = append(dp, newRow)
//	}
//
//	t := trace{map[int]map[int]int{}}
//
//	for i := 0; i < len(pars); i++ {
//		dp[i][i] = 1
//	}
//
//	fmt.Printf("%v", pars)
//	for l := 1; l < len(pars); l++ {
//		for i := l; i < len(pars); i++ {
//			j := i - l
//			left, right := dp[j+1][i]+1, dp[j][i-1]+1
//			mid := math.MaxInt
//			if s[pars[j]] == '(' && s[pars[i]] == ')' {
//				mid = dp[j+1][i-1]
//			}
//			if left <= right && left <= mid {
//				t.insert(j, i, 0)
//				dp[j][i] = left
//			} else if right <= left && right <= mid {
//				t.insert(j, i, 1)
//				dp[j][i] = right
//			} else {
//				t.insert(j, i, 2)
//				dp[j][i] = mid
//			}
//			//fmt.Printf("i %d, j %d, trace: %v\n", i, j, t.search(i,j))
//		}
//	}
//
//	fmt.Printf("dp: %v", dp)
//	fmt.Printf("trace: %v", t)
//
//	ret := ""
//	filterMap := parseTrace(t, pars,len(pars) - 1, 0)
//	fmt.Printf("filter %v\n",filterMap)
//	for i, _ := range s {
//		if _, ok := filterMap[i]; ok {
//			continue
//		}
//		ret += s[i:i+1]
//	}
//	return ret
//}
//
//type trace struct {
//	m map[int]map[int]int
//}
//
//func (t trace) insert(i, j, val int) {
//	if t.m == nil {
//		t.m = map[int]map[int]int{}
//	}
//	if _, ok := t.m[i]; !ok {
//		t.m[i] = map[int]int{}
//	}
//	t.m[i][j] = val
//}
//
//func (t trace) search(i, j int) int {
//	return t.m[i][j]
//}
//
//func parseTrace(t trace, pars []int, x, y int) map[int]bool {
//	idx := map[int]bool{}
//	fmt.Printf("trace %v\n", t)
//	for ; x >= y ; {
//		val := t.search(y, x)
//		fmt.Printf("x, y, val: %d, %d, %d\n", x, y,val)
//		if val == 0 {
//			idx[pars[y]] = true
//			y = y + 1
//		} else if val == 1 {
//			idx[pars[x]] = true
//			x = x - 1
//		} else if val == 2 {
//			x = x - 1
//			y = y + 1
//		}
//	}
//	return idx
//}

// Stack mock stack
type Stack struct {
	store []int
}

func (s *Stack) Push(val int) {
	if s.store == nil {
		s.store = []int{val}
		return
	}

	s.store = append(s.store, val)
}

func (s *Stack) Pop() (int, bool) {
	if s.store == nil || len(s.store) == 0 {
		return -1, false
	}
	ret := s.store[len(s.store)-1]
	s.store = s.store[:len(s.store)-1]
	return ret, true
}

func minRemoveToMakeValid(s string) string {
	stk := stack.Stack{}
	removeIdx := map[int]bool{}
	for i, b := range s {
		if b == '(' {
			stk.Push(i)
		} else if b == ')' {
			_, ok := stk.Pop()
			if !ok {
				removeIdx[i] = true
			}
		}
	}
	for i, ok := stk.Pop(); ok; i, ok = stk.Pop() {
		removeIdx[i] = true
	}

	ret := []byte{}
	for i, b := range s {
		if _, ok := removeIdx[i]; !ok {
			ret = append(ret, byte(b))
		}
	}
	return string(ret)
}
