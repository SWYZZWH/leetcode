# 443. String Compression
# Given an array of characters chars, compress it using the following algorithm:
#
# Begin with an empty string s. For each group of consecutive repeating characters in chars:
#
# If the group's length is 1, append the character to s.
# Otherwise, append the character followed by the group's length.
# The compressed string s should not be returned separately, but instead, be stored in the input character array chars. Note that group lengths that are 10 or longer will be split into multiple characters in chars.
#
# After you are done modifying the input array, return the new length of the array.
#
# You must write an algorithm that uses only constant extra space.
from typing import List


class Solution:
    def compress(self, chars: List[str]) -> int:
        i, j = 0, 0
        while i < len(chars):
            num = 0
            curChar = chars[i]
            while i < len(chars) and chars[i] == curChar:
                num += 1
                i += 1
            if num == 1:
                chars[j] = curChar
                j += 1
                continue
            chars[j] = curChar
            numStr = str(num)
            chars[j + 1: j + 1 + len(numStr)] = numStr
            j += len(numStr) + 1
        return j
