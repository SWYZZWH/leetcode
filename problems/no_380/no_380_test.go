package no_380

import "testing"

func Test380(t *testing.T) {
	randomizedSet := Constructor()
	randomizedSet.Insert(1)   // Inserts 1 to the set. Returns true as 1 was inserted successfully.
	randomizedSet.Remove(2)   // Returns false as 2 does not exist in the set.
	randomizedSet.Insert(2)   // Inserts 2 to the set, returns true. Set now contains [1,2].
	randomizedSet.GetRandom() // getRandom() should return either 1 or 2 randomly.
	randomizedSet.Remove(1)   // Removes 1 from the set, returns true. Set now contains [2].
	randomizedSet.Insert(2)   // 2 was already in the set, so return false.
	randomizedSet.GetRandom() // Since 2 is the only number in the set, getRandom() will always return 2.
}

func Test380_1(t *testing.T) {
	randomizedSet := Constructor()
	randomizedSet.Insert(0)   // Inserts 1 to the set. Returns true as 1 was inserted successfully.
	randomizedSet.Remove(0)   // Returns false as 2 does not exist in the set.
	randomizedSet.Insert(0)   // Inserts 2 to the set, returns true. Set now contains [1,2].
	randomizedSet.Remove(0)   // Returns false as 2 does not exist in the set.
	randomizedSet.Remove(0)   // Returns false as 2 does not exist in the set.
	randomizedSet.GetRandom() // Since 2 is the only number in the set, getRandom() will always return 2.
}
