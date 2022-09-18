class Solution:
    # start from any index with value 0 and run BFS from this index
    # [4, 3, 5, 3, 7, 6, 8]
    # [-4, -1, -1, 3, 1, 4, 4]
    # or we can simply run BFS from start
    # when BFS is working, then DFS might also work well
    def canReach(self, arr: List[int], start: int) -> bool:
        q = collections.deque([start])
        visited = set()

        while q:
            idx = q.pop()
            if idx >= len(arr) or idx < 0:
                continue
            if idx in visited:
                continue
            if arr[idx] == 0:
                return True
            visited.add(idx)
            q.append(idx + arr[idx])
            q.append(idx - arr[idx])

        return False