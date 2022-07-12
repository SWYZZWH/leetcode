package no_380

import "math/rand"

//380. Insert Delete GetRandom O(1)
// Implement the RandomizedSet class:
//
//RandomizedSet() Initializes the RandomizedSet object.
//bool insert(int val) Inserts an item val into the set if not present. Returns true if the item was not present, false otherwise.
//bool remove(int val) Removes an item val from the set if present. Returns true if the item was present, false otherwise.
//int getRandom() Returns a random element from the current set of elements (it's guaranteed that at least one element exists when this method is called). Each element must have the same probability of being returned.
//You must implement the functions of the class such that each function works in average O(1) time complexity.

// insert and GetRandom can achieve O(1) quite easily by map and array
// the most difficult part is how to delete an element in O(1)
// just exchange the element with the last element in array, and delete the last element!

type RandomizedSet struct {
	indexMap map[int]int
	keys     []int
}

func Constructor() RandomizedSet {
	return RandomizedSet{
		indexMap: map[int]int{},
		keys:     []int{},
	}
}

func (this *RandomizedSet) Insert(val int) bool {
	if _, ok := this.indexMap[val]; !ok {
		this.keys = append(this.keys, val)
		this.indexMap[val] = len(this.keys) - 1
		return true
	}
	return false
}

func (this *RandomizedSet) Remove(val int) bool {
	if idx, ok := this.indexMap[val]; !ok {
		return false
	} else {
		if idx != len(this.keys)-1 {
			// swap idx with len(this.keys) - 1
			this.keys[idx] = this.keys[len(this.keys)-1]
			this.indexMap[this.keys[idx]] = idx
		}
		this.keys = this.keys[:len(this.keys)-1]
		delete(this.indexMap, val)
		return true
	}
}

func (this *RandomizedSet) GetRandom() int {
	return this.keys[rand.Intn(len(this.keys))]
}
