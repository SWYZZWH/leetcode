package linkedList

import "testing"

func TestLinkedList(t *testing.T) {
	lst := LinkedList{}
	lst.AddValHead(1)
	lst.Show()
	lst.AddValHead(2)
	lst.Show()
	lst.AddAfter(lst.Head, 3)
	lst.Show()
	lst.AddBefore(lst.Head.Next, 4)
	lst.Show()
	lst.RemoveHead()
	lst.Show()
	lst.RemoveNode(lst.Head.Next.Next)
	lst.Show()
}

func TestDualLinkedList(t *testing.T) {
	dLst := DualLinkedList{}
	dLst.addHead(1)
	dLst.show()
	dLst.addHead(2)
	dLst.show()
	dLst.addBefore(dLst.head.next, 3)
	dLst.show()
	dLst.addAfter(dLst.head.next, 4)
	dLst.show()
	dLst.addTail(5)
	dLst.show()

	dLst.removeTail()
	dLst.show()
	dLst.removeHead()
	dLst.show()
	dLst.removeNode(dLst.head)
	dLst.show()
	dLst.removeNode(dLst.head.next)
	dLst.show()
	dLst.removeNode(dLst.tail)
	dLst.show()
}
