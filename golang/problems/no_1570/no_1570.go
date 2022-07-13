package no_1570

// 1570. Dot Product of Two Sparse Vectors

//Given two sparse vectors, compute their dot product.
//
//Implement class SparseVector:
//
//SparseVector(nums) Initializes the object with the vector nums
//dotProduct(vec) Compute the dot product between the instance of SparseVector and vec
//A sparse vector is a vector that has mostly zero values, you should store the sparse vector efficiently and compute the dot product between two SparseVector.
//
//Follow up: What if only one of the vectors is sparse?

type SparseVector struct {
	length int
	idx    map[int]int
}

func Constructor(nums []int) SparseVector {
	idx := map[int]int{}
	for i := 0; i < len(nums); i++ {
		if nums[i] == 0 {
			continue
		}
		idx[i] = nums[i]
	}
	return SparseVector{
		length: len(nums),
		idx:    idx,
	}
}

// Return the dotProduct of two sparse vectors
func (this *SparseVector) dotProduct(vec SparseVector) int {
	if vec.length < this.length {
		return vec.dotProduct(*this)
	}

	sum := 0
	for i, val := range this.idx {
		if val2, ok := vec.idx[i]; ok {
			sum += val * val2
		}
	}

	return sum
}

/**
 * Your SparseVector object will be instantiated and called as such:
 * v1 := Constructor(nums1);
 * v2 := Constructor(nums2);
 * ans := v1.dotProduct(v2);
 */
