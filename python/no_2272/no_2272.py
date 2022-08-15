# The variance of a string is defined as the largest difference between the
# number of occurrences of any 2 characters present in the string. Note the two
# characters may or may not be the same.
#
#  Given a string s consisting of lowercase English letters only, return the
# largest variance possible among all substrings of s.
#
#  A substring is a contiguous sequence of characters within a string.
#
#
#  Example 1:
#
#
# Input: s = "aababbb"
# Output: 3
# Explanation:
# All possible variances along with their respective substrings are listed
# below:
# - Variance 0 for substrings "a", "aa", "ab", "abab", "aababb", "ba", "b",
# "bb", and "bbb".
# - Variance 1 for substrings "aab", "aba", "abb", "aabab", "ababb", "aababbb",
# and "bab".
# - Variance 2 for substrings "aaba", "ababbb", "abbb", and "babb".
# - Variance 3 for substring "babbb".
# Since the largest possible variance is 3, we return it.
#
#
#  Example 2:
#
#
# Input: s = "abcde"
# Output: 0
# Explanation:
# No letter occurs more than once in s, so the variance of every substring is 0.
#
#
#
#
#  Constraints:
#
#
#  1 <= s.length <= 10⁴
#  s consists of lowercase English letters.
#
#
#  Related Topics Array Dynamic Programming 👍 337 👎 29


# leetcode submit region begin(Prohibit modification and deletion)
import math


class Solution:
    # consider string only have two letters: (a, b)
    # then the problem is the same as max subarray sum
    # visit all letter pairs (a, b), (a, c)....
    def largestVariance(self, s: str) -> int:
        counter = collections.Counter(s)
        letter = list(set(s))
        ret = 0

        def kadane(i: int, j: int, s: str) -> int:
            ret = 0
            flag_1, flag_2 = True, True
            cur_1, cur_2 = 0, 0
            remain_i, remain_j = counter[letter[i]], counter[letter[j]]
            # 1: i > j
            # 2: j > i
            for k in range(len(s)):
                remain_i -= s[k] == letter[i]
                remain_j -= s[k] == letter[j]

                cur_1 += (s[k] == letter[i]) - (s[k] == letter[j])
                cur_2 += (s[k] == letter[j]) - (s[k] == letter[i])

                flag_1 &= s[k] != letter[j]
                flag_2 &= s[k] != letter[i]

                if cur_1 < 0: cur_1 = 0; flag_1 = True
                if cur_2 < 0: cur_2 = 0; flag_2 = True

                ret = max(ret, cur_1 - flag_1)
                ret = max(ret, cur_2 - flag_2)

                # opt 1
                if remain_i == 0:
                    cur_2 += remain_j
                    ret = max(ret, cur_2 - flag_2)
                    break
                if remain_j == 0:
                    cur_1 += remain_i
                    ret = max(ret, cur_1 - flag_1)
                    break
            return ret

        # opt 2
        for i in range(len(letter) - 1):
            for j in range(i + 1, len(letter)):
                # opt 3
                new_str = [c for c in s if c == letter[i] or c == letter[j]]
                ret = max(ret, kadane(i, j, new_str))
        return ret
# leetcode submit region end(Prohibit modification and deletion)
