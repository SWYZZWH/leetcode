package no_121

// 121. Best Time to Buy and Sell Stock
// You are given an array prices where prices[i] is the price of a given stock on the ith day.
//
// You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.
//
// Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

// Solution 1 : brute force O(n ** 2)

// Solution 2 : like trap rain, from left to right, find the min before as min_i; from right to left, find the max after as max_i
// calculate profit: max_i - min_i
// time complexity O(2 * n) space complexity O(n)

// Solution 3: O(n) and O(1)
// just like maximum subarray

func max(a, b int) int {
	if a > b {
		return a
	}
	return b
}

func maxProfit(prices []int) int {
	ret := 0
	totalProfit := 0
	for i := 1; i < len(prices); i++ {
		profit := prices[i] - prices[i-1]
		if totalProfit+profit > 0 {
			totalProfit += profit
		} else {
			totalProfit = 0
		}
		ret = max(ret, totalProfit)
	}
	return ret
}
