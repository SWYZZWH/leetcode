# Roman numerals are represented by seven different symbols: I, V, X, L, C, D
# and M.
#
#
# Symbol       Value
# I             1
# V             5
# X             10
# L             50
# C             100
# D             500
# M             1000
#
#  For example, 2 is written as II in Roman numeral, just two one's added
# together. 12 is written as XII, which is simply X + II. The number 27 is written as
# XXVII, which is XX + V + II.
#
#  Roman numerals are usually written largest to smallest from left to right.
# However, the numeral for four is not IIII. Instead, the number four is written as
# IV. Because the one is before the five we subtract it making four. The same
# principle applies to the number nine, which is written as IX. There are six
# instances where subtraction is used:
#
#
#  I can be placed before V (5) and X (10) to make 4 and 9.
#  X can be placed before L (50) and C (100) to make 40 and 90.
#  C can be placed before D (500) and M (1000) to make 400 and 900.
#
#
#  Given an integer, convert it to a roman numeral.
#
#
#  Example 1:
#
#
# Input: num = 3
# Output: "III"
# Explanation: 3 is represented as 3 ones.
#
#
#  Example 2:
#
#
# Input: num = 58
# Output: "LVIII"
# Explanation: L = 50, V = 5, III = 3.
#
#
#  Example 3:
#
#
# Input: num = 1994
# Output: "MCMXCIV"
# Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.
#
#
#
#  Constraints:
#
#
#  1 <= num <= 3999
#
#
#  Related Topics Hash Table Math String 👍 3599 👎 4213


# leetcode submit region begin(Prohibit modification and deletion)
# brute force
class Solution:
    def intToRoman(self, num: int) -> str:
        ret = ""
        ms = num // 1000
        if ms != 0:
            ret += "M" * ms
        num %= 1000
        if num >= 900:
            ret += "CM"
            num -= 900
        elif num >= 500:
            ret += "D"
            num -= 500
        elif num >= 400:
            ret += "CD"
            num -= 400
        cs = num // 100  # must be 0-3
        if cs != 0:
            ret += "C" * cs
        num %= 100
        # now the num is under 100
        if num >= 90:
            ret += "XC"
            num -= 90
        elif num >= 50:
            ret += "L"
            num -= 50
        elif num >= 40:
            ret += "XL"
            num -= 40
        xs = num // 10  # must be 0-3
        if xs != 0:
            ret += "X" * xs
        num %= 10
        # now the num must be 0 - 9
        if num >= 9:
            ret += "IX"
            num -= 9
        elif num >= 5:
            ret += "V"
            num -= 5
        elif num >= 4:
            ret += "IV"
            num -= 4
        if num != 0:
            ret += "I" * num
        return ret
# leetcode submit region end(Prohibit modification and deletion)
