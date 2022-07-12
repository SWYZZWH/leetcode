package no_79

// 79. Word Search
// Given an m x n grid of characters board and a string word, return true if word exists in the grid.
//
//The word can be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or vertically neighboring. The same letter cell may not be used more than once.

// m == board.length
// n = board[i].length
// 1 <= m, n <= 6
// 1 <= word.length <= 15
// board and word consists of only lowercase and uppercase English letters.

// simple DFS
// backtracking (visited board, cleanup when all sub problems are dead)
func exist(board [][]byte, word string) bool {
	for i := 0; i < len(board); i++ {
		for j := 0; j < len(board[i]); j++ {
			visited := make([][]bool, len(board))
			for i := 0; i < len(board); i++ {
				for j := 0; j < len(board[i]); j++ {
					visited[i] = make([]bool, len(board[i]))
				}
			}
			if dfs(board, visited, i, j, word) {
				return true
			}
		}
	}
	return false
}
func dfs(board [][]byte, visited [][]bool, i, j int, word string) bool {
	if len(word) == 0 {
		return true
	}
	if i < 0 || i >= len(board) || j < 0 || j >= len(board[i]) {
		return false
	}
	if visited[i][j] {
		return false
	}
	if board[i][j] != word[0] {
		return false
	}
	visited[i][j] = true // notice! visited is true only if it is valid
	if dfs(board, visited, i+1, j, word[1:]) || dfs(board, visited, i-1, j, word[1:]) ||
		dfs(board, visited, i, j+1, word[1:]) || dfs(board, visited, i, j-1, word[1:]) {
		return true
	} else {
		visited[i][j] = false // if all sub are invalid, clean visited before return
		return false
	}
}
