package no_2

import (
	"awesomeProject/golang/utils/linkedList"
)

//2. Add Two Numbers
//You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.
//
//You may assume the two numbers do not contain any leading zero, except the number 0 itself.

//type ListNode struct {
//	Val  int
//	Next *ListNode
//}

func addTwoNumbers(l1 *linkedList.Node, l2 *linkedList.Node) *linkedList.Node {
	//total := 0
	carry := 0

	ret := linkedList.Node{
		Val:  -1,
		Next: nil,
	}
	p := &ret
	// handle common part
	for l1 != nil && l2 != nil {
		curSum := l1.Val + l2.Val + carry
		carry = curSum / 10
		curSum %= 10
		l1.Val = curSum
		p.Next = l1
		p = p.Next
		l1 = l1.Next
		l2 = l2.Next
		//total += curSum * math.Pow(10, digit)
	}
	// handle the rest
	for l1 != nil {
		curSum := l1.Val + carry
		carry = curSum / 10
		curSum %= 10
		l1.Val = curSum
		p.Next = l1
		l1 = l1.Next
		p = p.Next
	}

	for l2 != nil {
		curSum := l2.Val + carry
		carry = curSum / 10
		curSum %= 10
		l2.Val = curSum
		p.Next = l2
		l2 = l2.Next
		p = p.Next
	}

	if carry != 0 {
		p.Next = &linkedList.Node{
			Val:  carry,
			Next: nil,
		}
	}

	return ret.Next
}
