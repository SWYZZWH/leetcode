class Solution:
    def reorganizeString(self, s: str) -> str:
        # use counting sort to get better
        # use heap
        c = collections.Counter(s)
        h = [(-v, k) for k, v in c.items()]
        heapq.heapify(h)
        res = ""
        while len(h) > 1:
            e1 = heapq.heappop(h)
            e2 = heapq.heappop(h)
            res += e1[1] + e2[1]
            if e1[0] + 1 < 0:
                heapq.heappush(h, (e1[0] + 1, e1[1]))
            if e2[0] + 1 < 0:
                heapq.heappush(h, (e2[0] + 1, e2[1]))

        if h:
            if h[0][0] == -1:
                return res + h[0][1]
            else:
                return ""

        return res