import collections


class Solution:
    # simple BFS
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        m, n = len(image), len(image[0])
        q = collections.deque()
        q.append((sr, sc))

        visited = [[False for i in range(n)] for j in range(m)]

        while q:
            r, c = q.popleft()
            visited[r][c] = True

            if r - 1 >= 0 and not visited[r - 1][c] and image[r - 1][c] == image[r][c]:
                q.append((r - 1, c))
            if r + 1 < m and not visited[r + 1][c] and image[r + 1][c] == image[r][c]:
                q.append((r + 1, c))
            if c - 1 >= 0 and not visited[r][c - 1] and image[r][c - 1] == image[r][c]:
                q.append((r, c - 1))
            if c + 1 < n and not visited[r][c + 1] and image[r][c + 1] == image[r][c]:
                q.append((r, c + 1))

            # must edit in the end
            image[r][c] = color

        return image