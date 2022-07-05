package linkedList

import "testing"

func TestLinkedList(t *testing.T) {
	lst := LinkedList{}
	lst.addValHead(1)
	lst.show()
	lst.addValHead(2)
	lst.show()
	lst.addAfter(lst.head, 3)
	lst.show()
	lst.addBefore(lst.head.next, 4)
	lst.show()
	lst.removeHead()
	lst.show()
	lst.removeNode(lst.head.next.next)
	lst.show()
}

func TestDualLinkedList(t *testing.T) {
	dLst := DualLinkedList{}
	dLst.addHead(1)
	dLst.show()
	dLst.addHead(2)
	dLst.show()
	dLst.addBefore(dLst.head.next,3)
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
