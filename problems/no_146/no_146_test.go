package no_146

import (
	"testing"
)

func TestLRU(t *testing.T) {
	lRUCache := Constructor(2)
	lRUCache.showStat()
	lRUCache.Put(1, 1) // cache is {1=1}
	lRUCache.showStat()
	lRUCache.Put(2, 2) // cache is {1=1, 2=2}
	lRUCache.showStat()
	lRUCache.Get(1)    // return 1
	lRUCache.showStat()
	lRUCache.Put(3, 3) // LRU key was 2, evicts key 2, cache is {1=1, 3=3}
	lRUCache.showStat()
	lRUCache.Get(2)    // returns -1 (not found)
	lRUCache.showStat()
	lRUCache.Put(4, 4) // LRU key was 1, evicts key 1, cache is {4=4, 3=3}
	lRUCache.showStat()
	lRUCache.Get(1)    // return -1 (not found)
	lRUCache.showStat()
	lRUCache.Get(3)    // return 3
	lRUCache.showStat()
	lRUCache.Get(4)    // return 4
}

func TestLRU2(t *testing.T) {
	lRUCache := Constructor(2)
	lRUCache.showStat()
	lRUCache.Put(2, 1) // cache is {1=1}
	lRUCache.showStat()
	lRUCache.Put(1, 1) // cache is {1=1, 2=2}
	lRUCache.showStat()
	//lRUCache.Get(1)    // return 1
	//lRUCache.showStat()
	lRUCache.Put(2, 3) // LRU key was 2, evicts key 2, cache is {1=1, 3=3}
	lRUCache.showStat()
	//lRUCache.Get(2)    // returns -1 (not found)
	//lRUCache.showStat()
	lRUCache.Put(4, 1) // LRU key was 1, evicts key 1, cache is {4=4, 3=3}
	lRUCache.showStat()
	//lRUCache.Get(1)    // return -1 (not found)
	//lRUCache.showStat()
	lRUCache.Get(1)    // return 3
	lRUCache.showStat()
	lRUCache.Get(2)    // return 4
}