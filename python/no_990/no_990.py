from typing import List


class UnionFindSet:

    def __init__(self, n: int):
        self.uf = [i for i in range(n)]

    def find(self, i: int) -> int:
        parent = self.uf[i]
        if parent != i:
            self.uf[i] = self.find(parent)
        return self.uf[i]

    def merge(self, i: int, j: int):
        p_i, p_j = self.find(i), self.find(j)
        if p_i == p_j:
            return
        self.uf[p_j] = p_i


class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
        # parse equations
        # build map from variable names -> index
        variable_map = {}
        equals, inequals = [], []
        total_vars = 0
        for e in equations:
            v1, v2 = e[0], e[-1]
            is_equal = e[1:3] == "=="
            if v1 not in variable_map:
                variable_map[v1] = total_vars
                total_vars += 1
            if v2 not in variable_map:
                variable_map[v2] = total_vars
                total_vars += 1
            if is_equal:
                equals.append((variable_map[v1], variable_map[v2]))
            else:
                inequals.append((variable_map[v1], variable_map[v2]))

        uf = UnionFindSet(total_vars)
        # for equations with "=="
        for e in equals:
            uf.merge(e[0], e[1])

        # for inequations with "!="
        for e in inequals:
            if uf.find(e[0]) == uf.find(e[1]):
                return False

        return True




