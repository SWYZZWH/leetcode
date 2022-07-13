package no_1

import (
	"fmt"
	"testing"
)

func TestName(t *testing.T) {
	fmt.Printf("%v", twoSum([]int{2,7,11,15}, 9))
	fmt.Printf("%v", twoSum([]int{2,3,4}, 6))
	fmt.Printf("%v", twoSum([]int{3,3}, 6))

	fmt.Printf("%v", twoSum2([]int{2,7,11,15}, 9))
	fmt.Printf("%v", twoSum2([]int{2,3,4}, 6))
	fmt.Printf("%v", twoSum2([]int{3,3}, 6))
}