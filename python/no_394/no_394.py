import collections
import math


class Solution:
    # use stack
    # type 0: string
    # type 1: multiplier, a number
    def decodeString(self, s: str) -> str:
        i = 0
        stk = collections.deque()
        while i < len(s):
            if '0' <= s[i] <= '9':
                j = i
                while '0' <= s[j] <= '9':
                    j += 1
                num = int(s[i:j])
                stk.append((1, num))
                i = j + 1
                math.sqrt()
            elif s[i] == ']':
                # pop once
                cur_str = ""
                while stk and stk[-1][0] != 1:
                    _, part = stk.pop()
                    cur_str = part + cur_str
                if stk:
                    _, repeat = stk.pop()
                    cur_str = cur_str * repeat
                stk.append((0, cur_str))
                i += 1
            else:
                # just a normal string
                stk.append((0, s[i]))
                i += 1

        return "".join([item[1] for item in stk])