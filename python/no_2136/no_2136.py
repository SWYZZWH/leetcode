class Solution:
    # we always plant flowers with longest grow time
    # the reason is simple:
    #   we need at least sum(plantTime) no matter of growTime
    #   we can rearrange these plant time by any order, there always stands: plant time 1 < plant time 2 < plant time 3
    #   (cause each plant can be plant only after we have finished planting the plant before)
    #   then we append the grow time at the end of each grow time
    #   it's so clear that we have to put the longest grow time as early as possible
    def earliestFullBloom(self, plantTime: List[int], growTime: List[int]) -> int:
        h = []
        for i in range(len(plantTime)):
            heapq.heappush(h, (-growTime[i], plantTime[i]))

        ret = 0
        cur_sum = 0
        for i in range(len(plantTime)):
            g, p = heapq.heappop(h)
            cur_sum += p
            ret = max(ret, cur_sum - g)

        return ret