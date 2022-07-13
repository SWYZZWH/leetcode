package no_528

import (
	"math/rand"
)

//
//You are given a 0-indexed array of positive integers w where w[i] describes the weight of the ith index.
//
//You need to implement the function pickIndex(), which randomly picks an index in the range [0, w.length - 1] (inclusive) and returns it. The probability of picking an index i is w[i] / sum(w).
//
//For example, if w = [1, 3], the probability of picking index 0 is 1 / (1 + 3) = 0.25 (i.e., 25%), and the probability of picking index 1 is 3 / (1 + 3) = 0.75 (i.e., 75%).
//

type Solution struct {
	accum []int
}

func Constructor(w []int) Solution {
	accum := make([]int, len(w))
	for sum, i := 0, 0; i < len(w); i++ {
		sum += w[i]
		accum[i] = sum
	}
	return Solution{accum: accum}
}

// PickIndex use binary search
func (this *Solution) PickIndex() int {
	count := int(rand.Int31()) % this.accum[len(this.accum)-1]
	i, j := 0, len(this.accum)
	for {
		h := int(uint(i+j) >> 1) // avoid overflow when computing h
		// i ≤ h < j
		if h == 0 || count < this.accum[h] && count >= this.accum[h-1] {
			return h
		}
		if count >= this.accum[h] {
			i = h // preserves cmp(i-1) > 0
		} else {
			j = h - 1 // preserves cmp(j) <= 0
		}
	}
}
