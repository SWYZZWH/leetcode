package no_1

import (
	"fmt"
	"github.com/stretchr/testify/require"
	"testing"
)

func TestName(t *testing.T) {
	require.Equal(t, []int{0, 1}, twoSum2([]int{2,7,11,15}, 9))
	fmt.Printf("%v", twoSum([]int{2,7,11,15}, 9))
	fmt.Printf("%v", twoSum([]int{2,3,4}, 6))
	fmt.Printf("%v", twoSum([]int{3,3}, 6))

	fmt.Printf("%v", twoSum2([]int{2,7,11,15}, 9))
	fmt.Printf("%v", twoSum2([]int{2,3,4}, 6))
	fmt.Printf("%v", twoSum2([]int{3,3}, 6))
}