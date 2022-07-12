package hashSet

import "github.com/emirpasic/gods/sets/hashset"

func testSet() *hashset.Set {
	s1 := hashset.New()
	s2 := hashset.New()
	s1.Add(1)
	s1.Add(2)
	s2.Add(2)
	s2.Add(3)
	return s1.Intersection(s2)
}
