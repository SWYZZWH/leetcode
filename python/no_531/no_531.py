from typing import List


class Solution:
    # B W
    # B B
    def findLonelyPixel(self, picture: List[List[str]]) -> int:
        m, n = len(picture), len(picture[0])
        rows, cols = [0 for i in range(m)], [0 for j in range(n)]

        for i in range(m):
            for j in range(n):
                if picture[i][j] == "B":
                    rows[i] += 1
                    cols[j] += 1

        res = 0
        for i in range(m):
            for j in range(n):
                if picture[i][j] == "B" and rows[i] == 1 and cols[j] == 1:
                    res += 1

        return res