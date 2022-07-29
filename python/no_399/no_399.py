# You are given an array of variable pairs equations and an array of real
# numbers values, where equations[i] = [Ai, Bi] and values[i] represent the equation Ai
# / Bi = values[i]. Each Ai or Bi is a string that represents a single variable.
#
#  You are also given some queries, where queries[j] = [Cj, Dj] represents the
# jᵗʰ query where you must find the answer for Cj / Dj = ?.
#
#  Return the answers to all queries. If a single answer cannot be determined,
# return -1.0.
#
#  Note: The input is always valid. You may assume that evaluating the queries
# will not result in division by zero and that there is no contradiction.
#
#
#  Example 1:
#
#
# Input: equations = [["a","b"],["b","c"]], values = [2.0,3.0], queries = [["a",
# "c"],["b","a"],["a","e"],["a","a"],["x","x"]]
# Output: [6.00000,0.50000,-1.00000,1.00000,-1.00000]
# Explanation:
# Given: a / b = 2.0, b / c = 3.0
# queries are: a / c = ?, b / a = ?, a / e = ?, a / a = ?, x / x = ?
# return: [6.0, 0.5, -1.0, 1.0, -1.0 ]
#
#
#  Example 2:
#
#
# Input: equations = [["a","b"],["b","c"],["bc","cd"]], values = [1.5,2.5,5.0],
# queries = [["a","c"],["c","b"],["bc","cd"],["cd","bc"]]
# Output: [3.75000,0.40000,5.00000,0.20000]
#
#
#  Example 3:
#
#
# Input: equations = [["a","b"]], values = [0.5], queries = [["a","b"],["b","a"]
# ,["a","c"],["x","y"]]
# Output: [0.50000,2.00000,-1.00000,-1.00000]
#
#
#
#  Constraints:
#
#
#  1 <= equations.length <= 20
#  equations[i].length == 2
#  1 <= Ai.length, Bi.length <= 5
#  values.length == equations.length
#  0.0 < values[i] <= 20.0
#  1 <= queries.length <= 20
#  queries[i].length == 2
#  1 <= Cj.length, Dj.length <= 5
#  Ai, Bi, Cj, Dj consist of lower case English letters and digits.
#
#
#  Related Topics Array Depth-First Search Breadth-First Search Union Find
# Graph Shortest Path 👍 6142 👎 520


# leetcode submit region begin(Prohibit modification and deletion)
from typing import List

from sortedcontainers import sortedset


# we can also build a graph / state machine which node is "a", "b" and do dfs / bfs

class Solution:
    class UnionFind:

        def __init__(self, n):
            self.nums = [[i, 1.0] for i in range(n)]

        def find_parent(self, i) -> List[int]:
            # ratio = 1.0
            # while i != self.nums[i][0]:
            #     ratio *= self.nums[i][1]
            #     i = self.nums[i][0]
            # return i, ratio

            # optimization
            if i != self.nums[i][0]:
                root, ratio = self.find_parent(self.nums[i][0])
                self.nums[i] = [root, ratio * self.nums[i][1]]
            return self.nums[i]

        # merge j to i
        # ratio = i / j
        def merge(self, i, j, ratio):
            p_i, ratio_i = self.find_parent(i)
            p_j, ratio_j = self.find_parent(j)
            if p_i == p_j:
                return
            self.nums[p_j] = [p_i, ratio * ratio_i / ratio_j]

    # topological sorting
    # customized Union Find
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        idx_map = {}
        for i, eq in enumerate(equations):
            if eq[0] not in idx_map:
                idx_map[eq[0]] = len(idx_map)
            if eq[1] not in idx_map:
                idx_map[eq[1]] = len(idx_map)

        uf = self.UnionFind(len(idx_map))

        for i, eq in enumerate(equations):
            idx1, idx2 = idx_map[eq[0]], idx_map[eq[1]]
            uf.merge(idx1, idx2, values[i])

        ret = []
        for q in queries:
            if q[0] not in idx_map or q[1] not in idx_map:
                ret.append(-1)
                continue
            p_i, ratio_i = uf.find_parent(idx_map[q[0]])
            p_j, ratio_j = uf.find_parent(idx_map[q[1]])
            if p_i != p_j:
                ret.append(-1)
                continue
            ret.append(ratio_j / ratio_i)
        return ret
# leetcode submit region end(Prohibit modification and deletion)
