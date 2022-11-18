# https://leetcode.com/problems/basic-calculator/discuss/2017431/Stop-hating-parsing-problems-and-start-having-fun
import collections
from typing import List


def check_circle(n: int, edges: List[List[int]]) -> bool:
    G = collections.defaultdict(set)
    for edge in edges:
        G[edge[0]].add(edge[1])
        G[edge[1]].add(edge[0])

    visited = set()

    def dfs(cur: int, parent: int) -> bool:
        if cur in visited:
            return True

        visited.add(cur)
        for neighbor in G[cur]:
            if neighbor == parent:
                continue
            if dfs(neighbor, cur):
                return True

        return False

    for i in range(n):
        if i in visited:
            continue
        if dfs(i, i):
            return True

    return False


class Solution:
    # expr = factor +/- factor +/- factor
    # factor = +- number / +-(expr)
    # number = [0-9]+
    def calculate(self, s: str) -> int:
        s = s.replace(" ", "")
        op = {
            "+": lambda x, y: x + y,
            "-": lambda x, y: x - y
        }

        def expr(s: str, i: int) -> (int, int):
            res, i = factor(s, i)
            while i != len(s) and s[i] in op:
                op_func = op[s[i]]
                f, i = factor(s, i + 1)
                res = op_func(res, f)
            return res, i

        def factor(s: str, i: int) -> (int, int):
            if i == len(s):
                return 0, i
            if s[i] == "(":
                res, i = expr(s, i + 1)
                return res, i + 1
            if s[i] == "+":
                return factor(s, i + 1)
            if s[i] == "-":
                res, i = factor(s, i + 1)
                return -res, i
            res = 0
            while i < len(s) and s[i].isdigit():
                res *= 10
                res += int(s[i])
                i += 1
            return res, i

        res, i = expr(s, 0)
        return res


if __name__ == "__main__":
    print(check_circle(3, [[0, 1], [0, 2], [1, 3]]))
