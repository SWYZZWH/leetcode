# 799. Champagne Tower

# We stack glasses in a pyramid, where the first row has 1 glass, the second row has 2 glasses, and so on until the 100th row.  Each glass holds one cup of champagne.
#
# Then, some champagne is poured into the first glass at the top.  When the topmost glass is full, any excess liquid poured will fall equally to the glass immediately to the left and right of it.  When those glasses become full, any excess champagne will fall equally to the left and right of those glasses, and so on.  (A glass at the bottom row has its excess champagne fall on the floor.)
#
# For example, after one cup of champagne is poured, the top most glass is full.  After two cups of champagne are poured, the two glasses on the second row are half full.  After three cups of champagne are poured, those two cups become full - there are 3 full glasses total now.  After four cups of champagne are poured, the third row has the middle glass half full, and the two outside glasses are a quarter full, as pictured below.


# Constraints:
#
# 0 <= poured <= 109
# 0 <= query_glass <= query_row < 100

class Solution:
    # simulation method use dp,
    # math solution is impossible
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        dp = [0.0] * 101
        dp[0] = float(poured)
        for i in range(100):
            if i == query_row:
                return dp[query_glass] if dp[query_glass] < 1 else 1.0
            for j in reversed(range(i + 1)):
                if dp[j] > 1:
                    dp[j + 1] += (dp[j] - 1) / 2
                    dp[j] = (dp[j] - 1) / 2
                else:
                    dp[j] = 0
