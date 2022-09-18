from typing import List


class Solution:
    def validUtf8(self, data: List[int]) -> bool:
        def isZero(d: int, bit: int) -> bool:
            return ((d >> bit) & 1) == 0

        def check_behind(idx: int, cnt: int) -> bool:
            for i in range(idx + 1, idx + cnt + 1):
                if i >= len(data):
                    return False
                if isZero(data[i], 7) or not isZero(data[i], 6):
                    return False
            return True

        i = 0
        while i < len(data):
            # print(format(data[i], '08b'))
            if isZero(data[i], 7):
                i += 1
                continue
            else:
                if isZero(data[i], 6):
                    return False
                if isZero(data[i], 5):
                    if not check_behind(i, 1):
                        return False
                    i += 2
                else:
                    if isZero(data[i], 4):
                        if not check_behind(i, 2):
                            return False
                        i += 3
                    else:
                        if isZero(data[i], 3):
                            if not check_behind(i, 3):
                                return False
                            i += 4
                        else:
                            return False

        return True