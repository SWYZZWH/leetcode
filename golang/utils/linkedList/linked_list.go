package linkedList

import "fmt"

type Node struct {
	Val  int
	Next *Node
}

func (n Node) show() string {
	return fmt.Sprintf("Val: %v, Next:%v", n.Val, n.Next)
}

type DualNode struct {
	val  int
	next *DualNode
	prev *DualNode
}

func (n DualNode) Show() string {
	return fmt.Sprintf("Val: %v, prev: %v, Next:%v", n.val, n.prev, n.next)
}

type LinkedList struct {
	Head *Node
}

func (l *LinkedList) AddNodeHead(n *Node) {
	if n == nil {
		return
	}

	n.Next = l.Head
	l.Head = n
}

func (l *LinkedList) AddValHead(val int) {
	l.AddNodeHead(&Node{
		Val:  val,
		Next: nil,
	})
}

func (l *LinkedList) FindNodeByVal(val int) *Node {
	for node := l.Head; node != nil; node = node.Next {
		if node.Val == val {
			return node
		}
	}
	return nil
}

func (l *LinkedList) FindParent(n *Node) *Node {
	if n == nil || l.Head == nil {
		return nil
	}

	if n == l.Head {
		return nil
	}

	for node := l.Head; node != nil; node = node.Next {
		if node.Next == n {
			return node
		}
	}

	return nil
}

func (l *LinkedList) AddBefore(n *Node, val int) bool {
	if n == nil {
		return false
	}

	newNode := &Node{
		Val:  val,
		Next: n,
	}

	if n == l.Head {
		l.Head = newNode
		return true
	}

	if p := l.FindParent(n); p != nil {
		p.Next = newNode
	}
	return true
}

func (l *LinkedList) AddAfter(n *Node, val int) bool {
	if n == nil {
		return false
	}
	newNode := &Node{
		Val:  val,
		Next: n.Next,
	}
	n.Next = newNode
	return true
}

func (l *LinkedList) AddAfterVal(val int) bool {
	node := l.FindNodeByVal(val)
	if node == nil {
		return false
	}
	return l.AddAfter(node, val)
}

func (l *LinkedList) RemoveHead() {
	if l.Head == nil {
		return
	}

	l.Head = l.Head.Next
}

func (l *LinkedList) RemoveNode(n *Node) {
	if n == nil {
		return
	}

	if n == l.Head {
		l.RemoveHead()
	}

	if p := l.FindParent(n); p != nil {
		p.Next = n.Next
	}
}

func (l *LinkedList) sort() {

}

func (l LinkedList) Show() {
	if l.Head == nil {
		fmt.Printf("Head is : nil\n")
	} else {
		fmt.Printf("Head is : %s\n", l.Head.show())
	}

	if l.Head != nil {
		for n := l.Head.Next; n != nil; n = n.Next {
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
		fmt.Printf("Head is : nil\n")
	} else {
		fmt.Printf("Head is : %s\n", l.head.Show())
	}
	if l.tail == nil {
		fmt.Printf("tail is : nil\n")
	} else {
		fmt.Printf("tail is : %s\n", l.tail.Show())
	}

	if l.head != nil {
		for n := l.head.next; n != nil; n = n.next {
			fmt.Printf("\tnode is : %s\n", n.Show())
		}
	}
}
