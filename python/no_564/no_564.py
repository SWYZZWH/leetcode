# Given a string n representing an integer, return the closest integer (not
# including itself), which is a palindrome. If there is a tie, return the smaller one.
#
#
#  The closest is defined as the absolute difference minimized between two
# integers.
#
#
#  Example 1:
#
#
# Input: n = "123"
# Output: "121"
#
#
#  Example 2:
#
#
# Input: n = "1"
# Output: "0"
# Explanation: 0 and 2 are the closest palindromes but we return the smallest
# which is 0.
#
#
#
#  Constraints:
#
#
#  1 <= n.length <= 18
#  n consists of only digits.
#  n does not have leading zeros.
#  n is representing an integer in the range [1, 10¹⁸ - 1].
#
#
#  Related Topics Math String 👍 513 👎 1200


# leetcode submit region begin(Prohibit modification and deletion)
import math


class Solution:
    # if return digit length != n length
    #   then only possible return value is 99...99 or 10...01
    # else
    #   candidates will be xxxmxxx, xxx(m+1)xxx, xxx(m-1)xxx or xxxmmxxx, xxx(m+1)(m+1)xxx, xxx(m-1)(m-1)xxx
    #   notice: when m == 0, return value might be (x-1)99(x-1)
    def nearestPalindromic(self, n: str) -> str:
        k = len(n)
        if k == 0:
            return ""
        candidates = []
        if k != 1:
            candidates = [int("9" * (k - 1)), int("1" + "0" * (k - 2) + "1"), int("9" * k), int("1" + "0" * (k - 1) + "1")]

        mid = k // 2
        ca = n[: k // 2]
        for cand in [str(int(ca) - 1) if len(str(int(ca) - 1)) == len(ca) else ca, str(int(ca) + 1) if len(str(int(ca) + 1)) == len(ca) else ca, n[: k // 2]] if k > 2 else [n[: k // 2]]:
            res = ""
            for i in reversed(range(mid)):
                res += cand[i]
            if k % 2 == 0:
                new_cand = cand + res
                if new_cand[mid] > '0':
                    candidates.append(int(new_cand[:mid - 1] + chr(ord(new_cand[mid]) - 1) * 2 + new_cand[mid + 1:]))
                if new_cand[mid] < '9':
                    candidates.append(int(new_cand[:mid - 1] + chr(ord(new_cand[mid]) + 1) * 2 + new_cand[mid + 1:]))
                candidates.append(int(new_cand))
            if k % 2 != 0:
                new_cand = cand + n[mid] + res
                candidates.append(int(new_cand))
                if new_cand[mid] > '0':
                    candidates.append(int(new_cand[:mid] + chr(ord(new_cand[mid]) - 1) + new_cand[mid + 1:]))
                if new_cand[mid] < '9':
                    candidates.append(int(new_cand[:mid] + chr(ord(new_cand[mid]) + 1) + new_cand[mid + 1:]))

        cur_min = math.inf
        min_num = math.inf
        for c in candidates:
            if c == int(n):
                continue
            if abs(c - int(n)) == cur_min and c <= min_num:
                min_num = c
            if abs(c - int(n)) < cur_min:
                min_num = c
                cur_min = abs(c - int(n))

        return str(min_num)