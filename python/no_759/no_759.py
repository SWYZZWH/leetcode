import heapq


class Interval:
    def __init__(self, start: int = None, end: int = None):
        self.start = start
        self.end = end


class Solution:
    # sweep-line algorithm
    # --- --
    #  -- -
    #  -  ---
    # if we meet a start time of the interval, score += 1
    # if we meet the end time of the same interval, score -= 1
    # common empty time is intervals when score == 0

    def employeeFreeTime(self, schedule: '[[Interval]]') -> '[Interval]':
        jobs = []
        heapq.heapify(jobs)
        for ss in schedule:
            for s in ss:
                heapq.heappush(jobs, (s.start, 0))
                heapq.heappush(jobs, (s.end, 1))

        ret = []
        score = 0
        start_of_free = -1
        while len(jobs) != 0:
            job = heapq.heappop(jobs)
            if job[1] == 0:
                score += 1
            else:
                score -= 1
            if start_of_free == -1 and score == 0:
                start_of_free = job[0]
            elif start_of_free != -1 and score != 0:
                if job[0] != start_of_free:
                    ret.append(Interval(start_of_free, job[0]))
                start_of_free = -1

        return ret