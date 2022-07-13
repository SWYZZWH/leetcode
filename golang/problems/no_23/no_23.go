package no_23

import (
	"github.com/emirpasic/gods/maps/treemap"
)

// 23. Merge k Sorted Lists
// You are given an array of k linked-lists lists, each linked-list is sorted in ascending order.
//
// Merge all the linked-lists into one sorted linked-list and return it.

/**
 * Definition for singly-linked list.
 */

type ListNode struct {
	Val  int
	Next *ListNode
}

// merge two list at one time is also a good solution
// use TreeMap to reduce comparison cost
// use priority queue / heap may better, because its native support for duplicated keys
func mergeKLists(lists []*ListNode) *ListNode {
	if lists == nil || len(lists) == 0 {
		return nil
	}

	head := &ListNode{Val: -1, Next: nil}
	p := head
	tm := treemap.NewWithIntComparator()
	for i := 0; i < len(lists); i++ {
		if lists[i] == nil {
			continue
		}
		nodes, ok := tm.Get(lists[i].Val)
		if !ok {
			tm.Put(lists[i].Val, []int{i})
		} else {
			tm.Put(lists[i].Val, append(nodes.([]int), i))
		}
	}

	for true {
		k, v := tm.Min()
		if v == nil {
			return head.Next
		}
		minNodes := v.([]int)
		if minNodes == nil || len(minNodes) == 0 {
			return head.Next
		}
		node := minNodes[len(minNodes)-1]
		if len(minNodes) == 1 {
			tm.Remove(k)
		} else {
			tm.Put(k, minNodes[:len(minNodes)-1])
		}

		p.Next = lists[node]
		p = p.Next
		if next := lists[node].Next; next != nil {
			nodes, ok := tm.Get(next.Val)
			if !ok {
				tm.Put(next.Val, []int{node})
			} else {
				tm.Put(next.Val, append(nodes.([]int), node))
			}
			lists[node] = next
		}
	}
	return nil
}
