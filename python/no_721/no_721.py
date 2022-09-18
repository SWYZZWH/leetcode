class UnionFind:

    def __init__(self, n: int):
        self.uf = [i for i in range(n)]

    def union(self, i: int, j: int):
        if i > j:
            return self.union(j, i)
        r_i, r_j = self.find(i), self.find(j)
        self.uf[r_j] = r_i

    def find(self, i: int) -> int:
        while self.uf[i] != self.uf[self.uf[i]]:
            self.uf[i] = self.uf[self.uf[i]]
        return self.uf[i]

    def cnt(self) -> int:
        return sum([1 if self.uf[i] == i else 0 for i in range(len(self.uf))])


class Solution:
    # Union Find (Disjoint)
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        ret = []
        acc_set = [set(acc[1:]) for acc in accounts]
        n = len(accounts)
        m = {}
        uf = UnionFind(n)

        for i in range(n):
            for acc in acc_set[i]:
                if acc in m:
                    # print("union {} {}".format(i, m[acc]))
                    uf.union(i, m[acc])
                    # print(uf.uf)
                else:
                    m[acc] = i

        ret = [[] for i in range(n)]

        for i in range(n):
            ret[i].append(accounts[i][0])

        for k, v in m.items():
            # print(uf.find(v))
            ret[uf.find(v)].append(k)

        return [r[:1] + sorted(r[1:]) for r in ret if len(r) > 1]
