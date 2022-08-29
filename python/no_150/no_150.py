import collections
from typing import List


class Solution:
    # stack simulation
    def evalRPN(self, tokens: List[str]) -> int:
        if len(tokens) == 0:
            return 0

        stk = collections.deque()
        for token in tokens:
            if token == "+":
                l, r = stk.pop(), stk.pop()
                stk.append(l + r)
            elif token == "-":
                l, r = stk.pop(), stk.pop()
                stk.append(r - l)
            elif token == "*":
                l, r = stk.pop(), stk.pop()
                stk.append(l * r)
            elif token == "/":
                l, r = stk.pop(), stk.pop()
                neg = 1
                if l * r < 0:
                    neg = -1
                stk.append((abs(r) // abs(l)) * neg)
            else:
                stk.append(int(token))

        return stk[0]