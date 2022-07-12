package no_716

import (
	"container/list"
	"github.com/emirpasic/gods/maps/treemap"
)

//716. Max Stack
//Design a max stack data structure that supports the stack operations and supports finding the stack's maximum element.
//
//Implement the MaxStack class:
//
//MaxStack() Initializes the stack object.
//void push(int x) Pushes element x onto the stack.
//int pop() Removes the element on top of the stack and returns it.
//int top() Gets the element on the top of the stack without removing it.
//int peekMax() Retrieves the maximum element in the stack without removing it.
//int popMax() Retrieves the maximum element in the stack and removes it. If there is more than one maximum element, only remove the top-most one.
//You must come up with a solution that supports O(1) for each top call and O(logn) for each other call?
//
//Constraints:
//
//-107 <= x <= 107
//At most 104 calls will be made to push, pop, top, peekMax, and popMax.
//There will be at least one element in the stack when pop, top, peekMax, or popMax is called.

// naive solution costs O(N) complexity for Pop()
// to achieve O(logN) for each solution, we use TreeMap as index and double linked list for actual Stack for O(1) when removing
// the double linked list can't be replaced by array, although we have already implemented O(1) removal algorithm for array
// the reason is after removing one element, the index of other elements will change

//type StackNode struct {
//	lastMax int
//	val     int
//}
//
//type MaxStack struct {
//	max    int
//	maxIdx int
//	nodes  []StackNode
//}
//
//func Constructor() MaxStack {
//	return MaxStack{
//		max:    math.MaxInt,
//		maxIdx: -1,
//		nodes:  []StackNode{},
//	}
//}
//
//func (this *MaxStack) Push(x int) {
//	if this.maxIdx == -1 {
//		this.nodes = append(this.nodes, StackNode{
//			lastMax: -1,
//			val:     x,
//		})
//	} else {
//		if x > this.max {
//			this.nodes = append(this.nodes, StackNode{
//				lastMax: this.maxIdx,
//				val:     x,
//			})
//			this.maxIdx = len(this.nodes) - 1
//			this.max = x
//		} else {
//			this.nodes = append(this.nodes, StackNode{
//				lastMax: this.maxIdx,
//				val:     x,
//			})
//		}
//	}
//}
//
//func (this *MaxStack) Pop() int {
//	m := &treemap.Map{}
//	if m == nil {
//		return -1
//	} else {
//		return 0
//	}
//}
//
//func (this *MaxStack) Top() int {
//	return this.nodes
//}
//
//func (this *MaxStack) PeekMax() int {
//
//}
//
//func (this *MaxStack) PopMax() int {
//
//}

/**
 * Your MaxStack object will be instantiated and called as such:
 * obj := Constructor();
 * obj.Push(x);
 * param_2 := obj.Pop();
 * param_3 := obj.Top();
 * param_4 := obj.PeekMax();
 * param_5 := obj.PopMax();
 */

type MaxStack struct {
	index *treemap.Map
	stk   *list.List
}

func Constructor() MaxStack {
	return MaxStack{
		treemap.NewWithIntComparator(),
		list.New(),
	}
}

func (this *MaxStack) Push(x int) {
	e := this.stk.PushBack(x)
	curNodes, found := this.index.Get(x)
	if !found {
		this.index.Put(x, []*list.Element{e})
	} else {
		nodes := curNodes.([]*list.Element)
		nodes = append(nodes, e)
		this.index.Put(x, nodes)
	}
}

func (this *MaxStack) Pop() int {
	curNodes, _ := this.index.Get(this.Top())
	if nodeCnt := len(curNodes.([]*list.Element)); nodeCnt == 1 {
		this.index.Remove(this.Top())
	} else {
		this.index.Put(this.Top(), curNodes.([]*list.Element)[:nodeCnt-1])
	}
	ret := this.stk.Back().Value.(int)
	this.stk.Remove(this.stk.Back())
	return ret
}

func (this *MaxStack) Top() int {
	return this.stk.Back().Value.(int)
}

func (this *MaxStack) PeekMax() int {
	_, v := this.index.Max()
	e := v.([]*list.Element)[0]
	return e.Value.(int)
}

func (this *MaxStack) PopMax() int {
	k, v := this.index.Max()
	nodeCnt := len(v.([]*list.Element))
	node := v.([]*list.Element)[nodeCnt-1]
	ret := node.Value.(int)
	this.stk.Remove(node)
	this.index.Remove(ret)

	if nodeCnt == 1 {
		this.index.Remove(k)
	} else {
		this.index.Put(k, v.([]*list.Element)[:nodeCnt-1])
	}
	return k.(int)
}

/**
 * Your MaxStack object will be instantiated and called as such:
 * obj := Constructor();
 * obj.Push(x);
 * param_2 := obj.Pop();
 * param_3 := obj.Top();
 * param_4 := obj.PeekMax();
 * param_5 := obj.PopMax();
 */
