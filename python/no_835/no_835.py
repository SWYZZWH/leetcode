from typing import List


class Solution:
    def largestOverlap(self, img1: List[List[int]], img2: List[List[int]]) -> int:
        n = len(img1)
        res = 0
        ones_1, ones_2 = 0, 0
        for i in range(n):
            for j in range(n):
                ones_1 += 1 if img1[i][j] == 1 else 0
                ones_2 += 1 if img2[i][j] == 1 else 0

        for i in range(-n, n):
            for j in range(-n, n):
                cur = 0
                for r in range(n):
                    for c in range(n):
                        if r + i >= n or r + i < 0 or c + j >= n or c + j < 0 or img1[r + i][c + j] != 1 or img2[r][c] != 1:
                            continue
                        cur += 1
                res = max(cur, res)
                if res == min(ones_1, ones_2):
                    return res

        return res