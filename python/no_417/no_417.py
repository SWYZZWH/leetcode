# top-down dp
# use BFS will be more simple
class Solution:
    def __init__(self):
        self.dp = {}
        self.visited = []

    def rec(self, heights: List[List[int]], i: int, j: int):
        if (i, j) in self.dp:
            return self.dp[(i, j)]

        if self.visited[i][j]:
            return False, False

        self.visited[i][j] = True
        m, n = len(heights), len(heights[0])
        pa, al = False, False
        if i == m - 1 or j == n - 1:
            al = True
        if i == 0 or j == 0:
            pa = True
        if al and pa:
            self.dp[(i, j)] = pa, al
            self.visited[i][j] = False
            return pa, al

        if i - 1 >= 0 and heights[i][j] >= heights[i - 1][j]:
            pp, aa = self.rec(heights, i - 1, j)
            pa = pp or pa
            al = aa or al
        if al and pa:
            self.dp[(i, j)] = pa, al
            self.visited[i][j] = False
            return pa, al

        if j - 1 >= 0 and heights[i][j] >= heights[i][j - 1]:
            pp, aa = self.rec(heights, i, j - 1)
            pa = pp or pa
            al = aa or al
        if al and pa:
            self.dp[(i, j)] = pa, al
            self.visited[i][j] = False
            return pa, al

        if i + 1 < m and heights[i][j] >= heights[i + 1][j]:
            pp, aa = self.rec(heights, i + 1, j)
            pa = pp or pa
            al = aa or al
        if al and pa:
            self.dp[(i, j)] = pa, al
            self.visited[i][j] = False
            return pa, al

        if j + 1 < n and heights[i][j] >= heights[i][j + 1]:
            pp, aa = self.rec(heights, i, j + 1)
            pa = pp or pa
            al = aa or al

        self.visited[i][j] = False
        return pa, al

    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ret = []
        m, n = len(heights), len(heights[0])
        self.visited = [[False for j in range(n)] for i in range(m)]
        for i in range(m):
            for j in range(n):
                pa, al = self.rec(heights, i, j)
                self.dp[(i, j)] = pa, al
                if pa and al:
                    ret.append([i, j])
        # print(self.dp)
        return ret
