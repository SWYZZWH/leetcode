class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        start_pos = None
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    start_pos = (i, j)

        # extend the first island using bfs
        s = set()
        q = collections.deque([start_pos])

        def insert1(queue, i, j):
            if i < 0 or i >= m or j < 0 or j >= n:
                return
            if (i, j) in s:
                return
            if grid[i][j] == 0:
                return
            s.add((i, j))
            queue.append((i, j))

        while q:
            tmp = collections.deque()
            while q:
                i, j = q.popleft()
                s.add((i, j))
                insert1(tmp, i + 1, j)
                insert1(tmp, i, j + 1)
                insert1(tmp, i - 1, j)
                insert1(tmp, i, j - 1)
            q = tmp

        q = collections.deque(list(s))
        dist = 0

        def insert2(queue, i, j) -> bool:
            if i < 0 or i >= m or j < 0 or j >= n:
                return False
            if (i, j) in s:
                return False
            if (i, j) not in s:
                if grid[i][j] == 1:
                    return True
                if grid[i][j] == 0:
                    grid[i][j] = 1
                    s.add((i, j))
            queue.append((i, j))
            return False

        while q:
            tmp = collections.deque()
            while q:
                i, j = q.popleft()
                if insert2(tmp, i + 1, j) or insert2(tmp, i, j + 1) or insert2(tmp, i - 1, j) or insert2(tmp, i, j - 1):
                    return dist
            dist += 1
            q = tmp

        return dist