import collections
class Solution:
    # filter and erase impossible situations first
    # then count all elements in wrong places
    def minSwaps(self, s: str) -> int:
        n = len(s)
        c = collections.Counter(s)
        if not (c['0'] == c["1"] or c["0"] == c["1"] - 1 or c["0"] == c["1"] + 1):
            return -1

        def count_swaps(element: str, is_odd: bool) -> int:
            swaps = 0
            for i in range(n):
                if s[i] == element:
                    if is_odd and i % 2 == 0 or not is_odd and i % 2 != 0:
                        swaps += 1

            return swaps

        if n % 2 == 0:
            return min(count_swaps("1", True), count_swaps("1", False))
        else:
            if c['0'] > c["1"]:
                return count_swaps("0", False)
            else:
                return count_swaps("1", False)