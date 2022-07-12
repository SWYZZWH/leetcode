package no_2

import (
	"awesomeProject/utils/linkedList"
	"testing"
)

func Test2_0(t *testing.T) {
	lst1, lst2 := linkedList.LinkedList{}, linkedList.LinkedList{}
	lst1.AddValHead(1)
	lst1.AddValHead(2)
	lst1.AddValHead(3)
	lst1.AddValHead(4)
	lst2.AddValHead(9)
	lst2.AddValHead(9)
	lst2.AddValHead(9)
	linkedList.LinkedList{Head: addTwoNumbers(lst1.Head, lst2.Head)}.Show()
}

func Test2_1(t *testing.T) {
	lst1, lst2 := linkedList.LinkedList{}, linkedList.LinkedList{}
	lst1.AddValHead(0)
	lst2.AddValHead(9)
	lst2.AddValHead(9)
	lst2.AddValHead(9)
	linkedList.LinkedList{Head: addTwoNumbers(lst1.Head, lst2.Head)}.Show()
}

func Test2_2(t *testing.T) {
	lst1, lst2 := linkedList.LinkedList{}, linkedList.LinkedList{}
	lst1.AddValHead(0)
	lst2.AddValHead(0)
	linkedList.LinkedList{Head: addTwoNumbers(lst1.Head, lst2.Head)}.Show()
}

func Test2_3(t *testing.T) {
	lst1, lst2 := linkedList.LinkedList{}, linkedList.LinkedList{}
	lst1.AddValHead(4)
	lst2.AddValHead(6)
	linkedList.LinkedList{Head: addTwoNumbers(lst1.Head, lst2.Head)}.Show()
}

func Test2_4(t *testing.T) {
	lst1, lst2 := linkedList.LinkedList{}, linkedList.LinkedList{}
	lst1.AddValHead(4)
	lst1.AddValHead(4)
	lst2.AddValHead(6)
	lst2.AddValHead(6)
	lst2.AddValHead(6)
	linkedList.LinkedList{Head: addTwoNumbers(lst1.Head, lst2.Head)}.Show()
}
