package no_146

import "fmt"

// LRUCache1 try to use priority queue/ heap to solve this and fail
// while heap can be easy for pop and push
// it's hard for heap to delete a certain element in it

//type LRUCache1 struct {
//	heap  *myHeap.NodeHeap
//	index map[int]*myHeap.TsNode
//	cap   int
//	ts    int
//}
//
//func Constructor(capacity int) LRUCache1 {
//	return LRUCache1{heap: &myHeap.NodeHeap{}, index: map[int]*myHeap.TsNode{}, cap: capacity, ts: 0}
//}
//
//func (this *LRUCache1) Get(key int) int {
//	this.ts += 1
//	if this.index == nil || this.index[key] == nil {
//		fmt.Printf("Method Call: Get %v, result: %v\n", key, -1)
//		return -1
//	}
//	node := this.index[key]
//	node.Ts = this.ts
//	fmt.Printf("Method Call: Get %v, result: %v, node ts: %d\n", key, node.Val, node.Ts)
//	return node.Val
//}
//
//func (this *LRUCache1) Put(key int, value int) {
//	fmt.Printf("Method Call: Put %v, %v\n", key, value)
//	// recycle one
//	if (*this.heap).Len() >= this.cap {
//		node := heap.Pop(this.heap).(*myHeap.TsNode)
//		this.index[node.Key] = nil
//	}
//	this.ts += 1
//	// put in new one
//	newNode := myHeap.TsNode{Ts: this.ts, Key: key, Val: value}
//	heap.Push(this.heap, &newNode)
//	this.index[key] = &newNode
//}
//
//func (this *LRUCache1) showStat() {
//	fmt.Printf("len of lru: %d\n", (*this.heap).Len())
//	fmt.Printf("ts: %d\n", this.ts)
//	fmt.Printf("index: %v\n", this.index)
//	fmt.Printf("heap: %v\n", *this.heap)
//}

type LRUNode struct {
	key   int
	value int
	prev  *LRUNode
	next  *LRUNode
}

func (n LRUNode) showNode() string {
	return fmt.Sprintf("key: %v, value: %v, prev: %v, next:%v", n.key, n.value, n.prev, n.next)
}

type LRUCache struct {
	head  *LRUNode
	tail  *LRUNode
	cap   int
	count int
	index map[int]*LRUNode
}

func Constructor(capacity int) LRUCache {
	return LRUCache{cap: capacity, index: map[int]*LRUNode{}}
}

func (this *LRUCache) Get(key int) int {
	fmt.Printf("get %v\n", key)
	if node, ok := this.index[key]; ok && node != nil {
		// move to head
		if node.prev == nil {
			return node.value
		}
		if node == this.tail {
			this.tail = node.prev
		}
		node.prev.next = node.next
		if node.next != nil {
			node.next.prev = node.prev
		}

		node.next = this.head
		node.prev = nil
		this.head.prev = node
		this.head = node
		return node.value
	} else {
		return -1
	}
}

func (this *LRUCache) Put(key int, value int) {
	fmt.Printf("put %v, %v\n", key, value)
	if node, ok := this.index[key]; ok && node != nil {
		// update, move node to the head
		node.value = value
		if node.prev == nil {
			return
		}
		if node == this.tail {
			this.tail = node.prev
		}
		node.prev.next = node.next
		if node.next != nil {
			node.next.prev = node.prev
		}

		node.next = this.head
		node.prev = nil
		this.head.prev = node
		this.head = node
		return
	}

	// add new one
	newNode := &LRUNode{
		key:   key,
		value: value,
	}
	newNode.next = this.head
	newNode.prev = nil
	if this.head != nil {
		this.head.prev = newNode
		this.head = newNode
	} else {
		this.head = newNode
		this.tail = newNode
	}
	this.index[key] = newNode
	this.count++

	// evict one
	if this.count > this.cap {
		this.index[this.tail.key] = nil
		this.tail = this.tail.prev
		this.tail.next = nil
		this.count--
	}
}

func printList(head *LRUNode, tail *LRUNode) {
	if head == nil {
		fmt.Printf("head is : nil\n")
	} else {
		fmt.Printf("head is : %s\n", head.showNode())
	}
	if tail == nil {
		fmt.Printf("tail is : nil\n")
	} else {
		fmt.Printf("tail is : %s\n", tail.showNode())
	}

	if head != nil {
		for n := head.next; n != nil; n = n.next {
			fmt.Printf("\tnode is : %s\n", n.showNode())
		}
	}

}

func (this *LRUCache) showStat() {
	printList(this.head, this.tail)
}
