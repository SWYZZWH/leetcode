package no_200

// [200. Number of Islands](https://leetcode.com/problems/number-of-islands)
//
//DFS / BFS 都是从某一个点出发下探
//
//Disjoint Set Union 自底向下合并连通分量

func isWater(b byte) bool {
	return b == '0'
}

func numIslands(grid [][]byte) int {
	ret := 0
	for i, row := range grid {
		for j, col := range row {
			if isWater(col) {
				continue
			}
			exploreIsland(grid, i, j)
			ret += 1
		}
	}
	return ret
}

func exploreIsland(grid [][]byte, i, j int) {
	m, n := len(grid), len(grid[0])
	if i >= m || i < 0 || j >= n || j < 0 || isWater(grid[i][j]) {
		return
	}
	grid[i][j] = '0'
	exploreIsland(grid, i, j-1)
	exploreIsland(grid, i, j+1)
	exploreIsland(grid, i+1, j)
	exploreIsland(grid, i-1, j)
}
