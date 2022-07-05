package linkedList

import "fmt"

type Node struct {
	val  int
	next *Node
}

func (n Node) show() string {
	return fmt.Sprintf("val: %v, next:%v", n.val, n.next)
}

type DualNode struct {
	val  int
	next *DualNode
	prev *DualNode
}

func (n DualNode) show() string {
	return fmt.Sprintf("val: %v, prev: %v, next:%v", n.val, n.prev, n.next)
}

type LinkedList struct {
	head *Node
}

func (l *LinkedList) addNodeHead(n *Node) {
	if n == nil {
		return
	}

	n.next = l.head
	l.head = n
}

func (l *LinkedList) addValHead(val int) {
	l.addNodeHead(&Node{
		val:  val,
		next: nil,
	})
}

func (l *LinkedList) findNodeByVal(val int) *Node {
	for node := l.head; node != nil; node = node.next {
		if node.val == val {
			return node
		}
	}
	return nil
}

func (l *LinkedList) findParent(n *Node) *Node {
	if n == nil || l.head == nil {
		return nil
	}

	if n == l.head {
		return nil
	}

	for node := l.head; node != nil; node = node.next {
		if node.next == n {
			return node
		}
	}

	return nil
}

func (l *LinkedList) addBefore(n *Node, val int) bool {
	if n == nil {
		return false
	}

	newNode := &Node{
		val:  val,
		next: n,
	}

	if n == l.head {
		l.head = newNode
		return true
	}

	if p := l.findParent(n); p != nil {
		p.next = newNode
	}
	return true
}

func (l *LinkedList) addAfter(n *Node, val int) bool {
	if n == nil {
		return false
	}
	newNode := &Node{
		val:  val,
		next: n.next,
	}
	n.next = newNode
	return true
}

func (l *LinkedList) addAfterVal(val int) bool {
	node := l.findNodeByVal(val)
	if node == nil {
		return false
	}
	return l.addAfter(node, val)
}

func (l *LinkedList) removeHead() {
	if l.head == nil {
		return
	}

	l.head = l.head.next
}

func (l *LinkedList) removeNode(n *Node) {
	if n == nil {
		return
	}

	if n == l.head {
		l.removeHead()
	}

	if p := l.findParent(n); p != nil {
		p.next = n.next
	}
}

func (l *LinkedList) sort() {

}

func (l LinkedList) show() {
	if l.head == nil {
		fmt.Printf("head is : nil\n")
	} else {
		fmt.Printf("head is : %s\n", l.head.show())
	}

	if l.head != nil {
		for n := l.head.next; n != nil; n = n.next {
			fmt.Printf("\tnode is : %s\n", n.show())
		}
	}
}

type DualLinkedList struct {
	head *DualNode
	tail *DualNode
}

func (l *DualLinkedList) reverse() {

}

func (l *DualLinkedList) addHead(val int) {
	newNode := DualNode{
		val:  val,
		next: l.head,
		prev: nil,
	}

	if l.head != nil {
		l.head.prev = &newNode
	} else {
		l.tail = &newNode
	}
	l.head = &newNode
}

func (l *DualLinkedList) addTail(val int) {
	newNode := DualNode{
		val:  val,
		next: nil,
		prev: l.tail,
	}

	if l.tail != nil {
		l.tail.next = &newNode
	} else {
		l.head = &newNode
	}
	l.tail = &newNode
}

func (l *DualLinkedList) addAfter(node *DualNode, val int) bool {
	if node == nil {
		return false
	}

	if node == l.tail {
		l.addTail(val)
		return true
	}

	newNode := DualNode{
		val:  val,
		next: node.next,
		prev: node,
	}

	node.next.prev = &newNode
	node.next = &newNode
	return true
}

func (l *DualLinkedList) addBefore(node *DualNode, val int) bool {
	if node == nil {
		return false
	}

	if node == l.head {
		l.addHead(val)
		return true
	}

	newNode := DualNode{
		val:  val,
		next: node,
		prev: node.prev,
	}
	node.prev.next = &newNode
	node.prev = &newNode
	return true
}

func (l *DualLinkedList) removeHead() {
	if l.head == nil {
		return
	}

	if l.head == l.tail {
		l.head.prev = nil
		l.head.next = nil
		l.head = nil
		l.tail = nil
		return
	}

	l.head = l.head.next
	l.head.prev.prev = nil
	l.head.prev.next = nil
	l.head.prev = nil
}

func (l *DualLinkedList) removeTail() {
	if l.tail == nil {
		return
	}

	if l.head == l.tail {
		l.head.prev = nil
		l.head.next = nil
		l.head = nil
		l.tail = nil
		return
	}

	l.tail = l.tail.prev
	l.tail.next.prev = nil
	l.tail.next.next = nil
	l.tail.next = nil
}

func (l *DualLinkedList) removeNode(node *DualNode) bool {
	if node == nil {
		return false
	}

	if node == l.head {
		l.removeHead()
		return true
	}

	if node == l.tail {
		l.removeTail()
		return true
	}

	if node.prev != nil {
		node.prev.next = node.next
	}
	if node.next != nil {
		node.next.prev = node.prev
	}
	node.prev = nil
	node.next = nil
	return true
}

func (l *DualLinkedList) show() {
	if l.head == nil {
		fmt.Printf("head is : nil\n")
	} else {
		fmt.Printf("head is : %s\n", l.head.show())
	}
	if l.tail == nil {
		fmt.Printf("tail is : nil\n")
	} else {
		fmt.Printf("tail is : %s\n", l.tail.show())
	}

	if l.head != nil {
		for n := l.head.next; n != nil; n = n.next {
			fmt.Printf("\tnode is : %s\n", n.show())
		}
	}
}
