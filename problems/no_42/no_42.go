package no_42

//volume of water can be contained by each bar is decided by the highest bar on the left and right
//
//dynamic programming
//
//单调栈
//
//two pointer

type Bar struct {
	index  int
	height int
}

type Stack struct {
	store []Bar
}

func (s *Stack) Push(val Bar) {
	if s.store == nil {
		s.store = []Bar{val}
		return
	}

	s.store = append(s.store, val)
}

func (s *Stack) Pop() (Bar, bool) {
	if s.store == nil || len(s.store) == 0 {
		return Bar{}, false
	}
	ret := s.store[len(s.store)-1]
	s.store = s.store[:len(s.store)-1]
	return ret, true
}

func (s *Stack) Top() (Bar, bool) {
	if s.store == nil || len(s.store) == 0 {
		return Bar{}, false
	}
	return s.store[len(s.store)-1], true
}

func min(a, b int) int {
	if a < b {
		return a
	}
	return b
}

func max(a, b int) int {
	if a > b {
		return a
	}
	return b
}

func trap(height []int) int {
	stk := Stack{}
	ret := 0
	curMax := -1
	for i, h := range height {
		top, ok := stk.Top()
		if !ok {
			stk.Push(Bar{i, h})
			curMax = h
			continue
		}
		if h <= top.height {
			stk.Push(Bar{i, h})
		} else {
			idx := i
			for ; ok && h >= top.height; top, ok = stk.Top() {
				ret += (idx - top.index) * (min(curMax, h) - top.height)
				idx = top.index
				stk.Pop()
			}
			stk.Push(Bar{idx, h})
			curMax = max(curMax, h)
		}
	}
	return ret
}
