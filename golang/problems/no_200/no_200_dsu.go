package no_200

import (
	"awesomeProject/golang/utils/DSU"
)

func getIndex(i, j, n int) int {
	return i*n + j
}

// DFS
func numIslandsDsu(grid [][]byte) int {
	m, n := len(grid), len(grid[0])
	dsu := DSU.NewDSU(m*n + 1)
	for i, row := range grid {
		for j, col := range row {
			if isWater(col) {
				dsu.Union(getIndex(i, j, n), m*n)
				continue
			}
			if i-1 > 0 && !isWater(grid[i-1][j]) {
				dsu.Union(getIndex(i-1, j, n), getIndex(i, j, n))
			}
			if i+1 < m && !isWater(grid[i+1][j]) {
				dsu.Union(getIndex(i+1, j, n), getIndex(i, j, n))
			}
			if j-1 > 0 && !isWater(grid[i][j-1]) {
				dsu.Union(getIndex(i, j-1, n), getIndex(i, j, n))
			}
			if j+1 < n && !isWater(grid[i][j+1]) {
				dsu.Union(getIndex(i, j+1, n), getIndex(i, j, n))
			}
		}
	}
	return dsu.GetRootCnt() - 1
}
