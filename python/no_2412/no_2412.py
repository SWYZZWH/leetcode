class Solution:
    # yet another greedy
    def minimumMoney(self, transactions: List[List[int]]) -> int:
        increase = [(-t[0], t[1]) for t in transactions if t[1] - t[0] >= 0]
        decrease = [(t[1], t[0]) for t in transactions if t[1] - t[0] < 0]

        ini = 0
        cur = ini

        heapq.heapify(decrease)
        while decrease:
            t = heapq.heappop(decrease)
            if cur < t[1]:
                ini += t[1] - cur
                cur = t[1]
            cur = cur - t[1] + t[0]

        heapq.heapify(increase)
        while increase:
            t = heapq.heappop(increase)
            if cur < -t[0]:
                ini += -t[0] - cur
                cur = -t[0]
            cur = cur + t[0] + t[1]

        return ini