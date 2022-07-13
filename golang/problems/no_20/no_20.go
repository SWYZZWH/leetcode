package no_20

// Stack mock stack
type Stack struct {
	store []byte
}

func (s *Stack) Push(val byte) {
	if s.store == nil {
		s.store = []byte{val}
		return
	}

	s.store = append(s.store, val)
}

func (s *Stack) Pop() (byte, bool) {
	if s.store == nil || len(s.store) == 0 {
		return ' ', false
	}
	ret := s.store[len(s.store)-1]
	s.store = s.store[:len(s.store)-1]
	return ret, true
}

func isValid(s string) bool {
	stk := Stack{}
	for _, b := range s {
		if b == '(' {
			stk.Push('(')
		} else if b == '[' {
			stk.Push('[')
		} else if b == '{' {
			stk.Push('{')
		} else if b == ')' {
			bb, ok := stk.Pop()
			if !ok || bb != '(' {
				return false
			}
		} else if b == ']' {
			bb, ok := stk.Pop()
			if !ok || bb != '[' {
				return false
			}
		} else if b == '}' {
			bb, ok := stk.Pop()
			if !ok || bb != '{' {
				return false
			}
		} else {
			return false
		}
	}
	if len(stk.store) != 0 {
		return false
	}
	return true
}
