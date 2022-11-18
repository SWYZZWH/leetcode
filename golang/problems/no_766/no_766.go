package no_766

func isToeplitzMatrix(matrix [][]int) bool {
	m, n := len(matrix), len(matrix[0])
	for l := 0; l < m ; l += 1 {
		i, j := l, 0
		ini := matrix[i][j]
		for i >= 0 && i < m && j >= 0 && j < n {
			if ini != matrix[i][j] {
				return false
			}

			i += 1
			j += 1
		}
	}

	for l := 0; l < n; l += 1 {
		i, j := 0, l
		ini := matrix[i][j]
		for i >= 0 && i < m && j >= 0 && j < n {
			if ini != matrix[i][j] {
				return false
			}

			i += 1
			j += 1
		}
	}
	return true
}