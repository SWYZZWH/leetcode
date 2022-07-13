package no_21

//You are given the heads of two sorted linked lists list1 and list2.
//
//Merge the two lists in a one sorted list. The list should be made by splicing together the nodes of the first two lists.
//
//Return the head of the merged linked list.

type ListNode struct {
	Val  int
	Next *ListNode
}

// classic solution
func mergeTwoLists(list1 *ListNode, list2 *ListNode) *ListNode {
	h := &ListNode{
		-1,
		nil,
	}
	p := h
	for list1 != nil && list2 != nil {
		if list1.Val < list2.Val {
			p.Next = list1
			list1 = list1.Next
		} else {
			p.Next = list2
			list2 = list2.Next
		}
	}

	for list1 != nil {
		p.Next = list1
		list1 = list1.Next
	}

	for list2 != nil {
		p.Next = list2
		list2 = list2.Next
	}

	return h.Next
}
