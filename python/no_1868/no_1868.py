from typing import List


class Solution:
    # do not expand into full arrays ...
    # two pointers
    def findRLEArray(self, encoded1: List[List[int]], encoded2: List[List[int]]) -> List[List[int]]:
        ret = []
        i, j = 0, 0
        cnt1, cnt2 = 0, 0
        while i < len(encoded1) and j < len(encoded2):
            res = min(encoded1[i][1] - cnt1, encoded2[j][1] - cnt2)
            mul = encoded1[i][0] * encoded2[j][0]
            if ret and ret[-1][0] == mul:
                ret[-1][1] += res
            else:
                ret.append([mul, res])
            if res + cnt1 == encoded1[i][1]:
                cnt1 = 0
                i += 1
            else:
                cnt1 += res
            if res + cnt2 == encoded2[j][1]:
                cnt2 = 0
                j += 1
            else:
                cnt2 += res
        return ret