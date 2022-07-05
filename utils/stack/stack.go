package stack

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

func (s *Stack) Top() (int, bool) {
	if s.store == nil || len(s.store) == 0 {
		return -1, false
	}
	return s.store[len(s.store)-1], true
}