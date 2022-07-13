package no_56

import (
	"fmt"
	"testing"
)

func TestMergeInterval(t *testing.T) {
	fmt.Printf("%v", merge([][]int{[]int{1, 3}, []int{2, 6}, []int{8, 10}, []int{15, 18}}))
	fmt.Printf("%v", merge([][]int{[]int{1, 4}, []int{4, 5}}))
	fmt.Printf("%v", merge([][]int{[]int{1, 4}}))
	fmt.Printf("%v", merge([][]int{[]int{1, 4}, {2, 3}}))
	fmt.Printf("%v", merge([][]int{[]int{1, 4}, {4, 4}}))
}
