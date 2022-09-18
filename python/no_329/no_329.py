from typing import List


class Solution:
    # graph problem!
    # edges (i, j) exists if and only if matrix[i] < matrix[j]
    # so this is a DAG and thus it can run topological sort
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        m, n = len(matrix), len(matrix[0])
        ret = [0]

        @functools.cache
        def dfs(i: int, j: int) -> int:
            if i < 0 or j < 0 or i >= m or j >= n:
                return 0
            max_len = 1
            if i - 1 >= 0 and matrix[i - 1][j] > matrix[i][j]:
                max_len = max(max_len, dfs(i - 1, j) + 1)
            if i + 1 < m and matrix[i + 1][j] > matrix[i][j]:
                max_len = max(max_len, dfs(i + 1, j) + 1)
            if j - 1 >= 0 and matrix[i][j - 1] > matrix[i][j]:
                max_len = max(max_len, dfs(i, j - 1) + 1)
            if j + 1 < n and matrix[i][j + 1] > matrix[i][j]:
                max_len = max(max_len, dfs(i, j + 1) + 1)
            ret[0] = max(ret[0], max_len)
            return max_len

        for i in range(m):
            for j in range(n):
                dfs(i, j)

        return ret[0]
