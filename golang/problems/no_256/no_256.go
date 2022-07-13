package no_256

//256. Paint House

//There is a row of n houses, where each house can be painted one of three colors: red, blue, or green. The cost of painting each house with a certain color is different. You have to paint all the houses such that no two adjacent houses have the same color.
//
//The cost of painting each house with a certain color is represented by an n x 3 cost matrix costs.
//
//For example, costs[0][0] is the cost of painting house 0 with the color red; costs[1][2] is the cost of painting house 1 with color green, and so on...
//Return the minimum cost to paint all houses.

// 1D dp problem
// dp[i][0] means the minimum cost of painting 0-i houses, when the house i is red
// dp[i][0] = costs[i][0] + max(cost[i-1][1], cost[i-1][2])

func min(a, b int) int {
	if a < b {
		return a
	}
	return b
}

func minCost(costs [][]int) int {
	if costs == nil || len(costs) == 0 {
		return 0
	}
	red, green, blue := costs[0][0], costs[0][1], costs[0][2]
	for i := 1; i < len(costs); i++ {
		redNew, greenNew, blueNew := min(green, blue)+costs[i][0], min(red, blue)+costs[i][1], min(green, red)+costs[i][2]
		red, green, blue = redNew, greenNew, blueNew
	}
	return min(min(red, green), blue)
}
