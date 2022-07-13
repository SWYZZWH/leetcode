package algorithms

// binary search can be referred as search.Find()
// if cmp(h) == 0, should directly return
// if cmp(h) > 0 || cmp (h) < 0, i or j must make an extra +1 / -1 move, or may be trapped in the dead loop
// the question is : i = h + 1 or j = h - 1 ?
// the key equation: i <= h < j, this equation stands every iteration, i.e. s(i) <= s(h) < s(j)
// if we let j = h - 1, and the target is k ,then there will be some chance j = k = h - 1, in next iterations, h can never be k,
// we must choose i = h + 1 and j = h

// find vars must be sorted before
func find(vars []int, target int) (int, bool) {
	if vars == nil || len(vars) == 0 {
		return -1, false
	}

	i, j := 0, len(vars)
	for i < j {
		h := int(uint(i+j) >> 1)
		if vars[h] == target {
			return h, true
		}
		if vars[h] < target {
			i = h + 1
		} else {
			j = h
		}
	}
	return i, i < len(vars) && vars[i] == target
}
