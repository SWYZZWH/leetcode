import collections
import itertools


class Solution:
    # simplest way is use a stack, however, this leads to a waste of space
    def backspaceCompare(self, s: str, t: str) -> bool:
        stk1, stk2 = collections.deque(), collections.deque()
        for i in range(len(s)):
            stk1.append(s[i])
        for j in range(len(t)):
            stk2.append(t[j])

        while stk1 and stk2:
            next_c_1, next_c_2 = "", ""
            cnt_1, cnt_2 = 0, 0
            while next_c_1 == "" and stk1:
                c = stk1.pop()
                if c == "#":
                    cnt_1 += 1
                else:
                    if cnt_1 == 0:
                        next_c_1 = c
                    else:
                        cnt_1 -= 1
            while next_c_2 == "" and stk2:
                c = stk2.pop()
                if c == "#":
                    cnt_2 += 1
                else:
                    if cnt_2 == 0:
                        next_c_2 = c
                    else:
                        cnt_2 -= 1
            if next_c_1 != next_c_2:
                return False

        cnt_1, cnt_2 = 0, 0
        while stk1:
            c = stk1.pop()
            if c == "#":
                cnt_1 += 1
            else:
                if cnt_1 == 0:
                    return False
                else:
                    cnt_1 -= 1

        while stk2:
            c = stk2.pop()
            if c == "#":
                cnt_2 += 1
            else:
                if cnt_2 == 0:
                    return False
                else:
                    cnt_2 -= 1

        return not stk1 and not stk2


class Solution:
    # best way is go from back to top, thus space complexity is O(1)
    def backspaceCompare(self, s: str, t: str) -> bool:
        i, j = len(s) - 1, len(t) - 1
        while i >= 0 and j >= 0:
            # continue to find a valid char
            next_c_1, next_c_2 = "", ""
            cnt_1, cnt_2 = 0, 0
            while next_c_1 == "" and i >= 0:
                if s[i] == "#":
                    cnt_1 += 1
                else:
                    if cnt_1 == 0:
                        next_c_1 = s[i]
                    else:
                        cnt_1 -= 1
                i -= 1
            while next_c_2 == "" and j >= 0:
                if t[j] == "#":
                    cnt_2 += 1
                else:
                    if cnt_2 == 0:
                        next_c_2 = t[j]
                    else:
                        cnt_2 -= 1
                j -= 1
            if next_c_1 != next_c_2:
                return False

        cnt_1, cnt_2 = 0, 0
        while i >= 0:
            if s[i] == "#":
                cnt_1 += 1
            else:
                if cnt_1 == 0:
                    return False
                else:
                    cnt_1 -= 1
            i -= 1

        while j >= 0:
            if t[j] == "#":
                cnt_2 += 1
            else:
                if cnt_2 == 0:
                    return False
                else:
                    cnt_2 -= 1
            j -= 1

        return i < 0 and j < 0


# elegant
class Solution(object):
    def backspaceCompare(self, S, T):
        def F(S):
            skip = 0
            for x in reversed(S):
                if x == '#':
                    skip += 1
                elif skip:
                    skip -= 1
                else:
                    yield x

        return all(x == y for x, y in itertools.zip_longest(F(S), F(T)))
