package no_339

//339. Nested List Weight Sum

//You are given a nested list of integers nestedList. Each element is either an integer or a list whose elements may also be integers or other lists.
//
//The depth of an integer is the number of lists that it is inside of. For example, the nested list [1,[2,2],[[3],2],1] has each integer's value set to its depth.
//
//Return the sum of each integer in nestedList multiplied by its depth.

/**
 * // This is the interface that allows for creating nested lists.
 * // You should not implement it, or speculate about its implementation
 * type NestedInteger struct {
 * }
 *
 * // Return true if this NestedInteger holds a single integer, rather than a nested list.
 * func (n NestedInteger) IsInteger() bool {}
 *
 * // Return the single integer that this NestedInteger holds, if it holds a single integer
 * // The result is undefined if this NestedInteger holds a nested list
 * // So before calling this method, you should have a check
 * func (n NestedInteger) GetInteger() int {}
 *
 * // Set this NestedInteger to hold a single integer.
 * func (n *NestedInteger) SetInteger(value int) {}
 *
 * // Set this NestedInteger to hold a nested list and adds a nested integer to it.
 * func (n *NestedInteger) Add(elem NestedInteger) {}
 *
 * // Return the nested list that this NestedInteger holds, if it holds a nested list
 * // The list length is zero if this NestedInteger holds a single integer
 * // You can access NestedInteger's List element directly if you want to modify it
 * func (n NestedInteger) GetList() []*NestedInteger {}
 */

type NestedInteger struct {
}

func (n NestedInteger) IsInteger() bool {
	return false
}

func (n NestedInteger) GetInteger() int {
	return -1
}

func (n *NestedInteger) Add(elem NestedInteger) {

}

func (n NestedInteger) GetList() []*NestedInteger {
	return nil
}

// go dfs
func depthSum(nestedList []*NestedInteger) int {
	sum := 0
	if nestedList == nil || len(nestedList) == 0 {
		return sum
	}

	for _, integer := range nestedList {
		if integer == nil {
			continue
		}
		sum += dfs(*integer, 1)
	}

	return sum
}

func dfs(i NestedInteger, depth int) int {
	if i.IsInteger() {
		return depth * i.GetInteger()
	}

	sum := 0
	for _, integer := range i.GetList() {
		if integer == nil {
			continue
		}
		sum += dfs(*integer, depth+1)
	}
	return sum
}
