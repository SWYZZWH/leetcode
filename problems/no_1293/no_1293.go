package no_1293

import "math"

// 1293. Shortest Path in a Grid with Obstacles Elimination
// You are given an m x n integer matrix grid where each cell is either 0 (empty) or 1 (obstacle). You can move up, down, left, or right from and to an empty cell in one step.
//
// Return the minimum number of steps to walk from the upper left corner (0, 0) to the lower right corner (m - 1, n - 1) given that you can eliminate at most k obstacles. If it is not possible to find such walk return -1.

// m == grid.length
//n == grid[i].length
//1 <= m, n <= 40
//1 <= k <= m * n
//grid[i][j] is either 0 or 1.
//grid[0][0] == grid[m - 1][n - 1] == 0

// DFS will cause stack overflow
// try dp, dp[m-1][n-1] = 0, 3D dp, i, j, k
// naive dp can't work, cause the possible routes are uncertain
// try bfs from the target to the source, use dp to save state
// grid 0 for unvisited, 1 for obstacles, 2 for visited

type posInfo struct {
	i int
	j int
	k int
}

func shortestPath(grid [][]int, k int) int {
	m, n := len(grid), len(grid[0])
	if k > m + n - 2{
		return m + n - 2
	}
	dp := make([][][]int, m)
	for i := 0; i < m; i++ {
		dp[i] = make([][]int, n)
		for j := 0; j < n; j++ {
			dp[i][j] = make([]int, k + 1)
			for l := 0; l < k + 1; l++ {
				dp[i][j][l] = math.MaxInt32
			}
		}
	}
	dp[0][0][0] = 0
	// bfs and save k
	level := 0
	q := []posInfo{{0, 0, 0}}
	for len(q) > 0 {
		tmpQueue := make([]posInfo, 0)
		for len(q) > 0 {
			node := q[len(q)-1]
			q = q[:len(q)-1]
			if node.i-1 >=0 {
				if updateDP(grid, dp, node, k, 0) {
					tmpQueue = append(tmpQueue, posInfo{node.i - 1, node.j, dp[node.i-1][node.j][1]})
				}
			}
			if node.i+1 <m {
				if updateDP(grid, dp, node, k, 1) {
					tmpQueue = append(tmpQueue, posInfo{node.i + 1, node.j, dp[node.i+1][node.j][1]})
				}
			}
			if node.j-1 >= 0 {
				if updateDP(grid, dp, node, k, 2) {
					tmpQueue = append(tmpQueue, posInfo{node.i, node.j - 1, dp[node.i][node.j-1][1]})
				}
			}
			if node.j+1 < n {
				if updateDP(grid, dp, node, k, 3) {
					tmpQueue = append(tmpQueue, posInfo{node.i, node.j + 1, dp[node.i][node.j+1][1]})
				}
			}
		}
		q = tmpQueue
		level++
	}

	minDist := math.MaxInt32
	for s := 0; s < k + 1; s++ {
		if dp[m-1][n-1][s] != math.MaxInt32{
			minDist = min(dp[m-1][n-1][s], minDist)
		}
	}

	if minDist == math.MaxInt32{
		return -1
	}

	return minDist
}

func updateDP(grid [][]int, dp [][][]int, node posInfo, maxLevel, dir int) bool {
	m, n := len(dp), len(dp[0])
	i, j := node.i, node.j
	updateI, updateJ := i, j
	if dir == 0 {
		updateI--
	} else if dir == 1 {
		updateI++
	} else if dir == 2 {
		updateJ--
	} else if dir == 3 {
		updateJ++
	}

	if updateI >= m || updateI < 0 || updateJ >= n || updateJ < 0 {
		return false
	}

	updated := false
	for s := 0; s < maxLevel + 1; s++ {
		if grid[updateI][updateJ] == 1 {
			if s+1 <= maxLevel && dp[i][j][s]+1 < dp[updateI][updateJ][s+1] {
				dp[updateI][updateJ][s+1] = dp[i][j][s] + 1
				updated = true
			}
		} else {
			if dp[i][j][s]+1 < dp[updateI][updateJ][s] {
				dp[updateI][updateJ][s] = dp[i][j][s] + 1
				updated = true
			}
		}
	}
	return updated
}

//func shortestPath(grid [][]int, k int) int {
//	// if k >= m + n - 2, can ignore obstacles
//	m, n := len(grid), len(grid[0])
//	dp := make([][][]int, m)
//	for i := 0; i < m; i++ {
//		dp[i] = make([][]int, n)
//		for j := 0; j < n; j++ {
//			dp[i][j] = make([]int, k)
//			for l := 0; l < k; l++ {
//				dp[i][j][l] = math.MaxInt8
//			}
//		}
//	}
//
//	for l := m + n - 2; l >= 0; l-- {
//		var i, j int
//		if l >= m {
//			i, j = m-1, l-m+1
//		} else {
//			i, j = l, 0
//		}
//
//		for i >= 0 && i < m && j >= 0 && j < n {
//			if i == m-1 && j == n-1 {
//				dp[i][j][0] = 0
//				break
//			}
//
//			// right and down
//			if i+1 < m {
//				for s := 0; s < len(dp[i+1][j]); s++ {
//					if dp[i+1][j][s] != -1 {
//						if grid[i][j] == 1 && s+1 < k {
//							dp[i][j][s+1] = min(dp[i][j][s+1], dp[i+1][j][s]+1)
//						} else if grid[i][j] == 0 {
//							dp[i][j][s] = min(dp[i][j][s], dp[i+1][j][s]+1)
//						}
//					}
//				}
//			}
//
//			if j+1 < n {
//				for s := 0; s < len(dp[i][j+1]); s++ {
//					if dp[i][j+1][s] != -1 {
//						if grid[i][j] == 1 && s+1 < k {
//							dp[i][j][s+1] = min(dp[i][j][s+1], dp[i][j+1][s]+1)
//						} else if grid[i][j] == 0 {
//							dp[i][j][s] = min(dp[i][j][s], dp[i][j+1][s]+1)
//						}
//					}
//				}
//			}
//			i--
//			j++
//		}
//	}
//
//	ret := math.MaxInt8
//	for i := 0; i < len(dp[0][0]); i++ {
//		ret = min(ret, dp[0][0][i])
//	}
//	return ret
//}

func min(a, b int) int {
	if a < b {
		return a
	}
	return b
}
