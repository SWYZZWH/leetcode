# 636. Exclusive Time of Functions

# On a single-threaded CPU, we execute a program containing n functions. Each function has a unique ID between 0 and n-1.
#
# Function calls are stored in a call stack: when a function call starts, its ID is pushed onto the stack, and when a function call ends, its ID is popped off the stack. The function whose ID is at the top of the stack is the current function being executed. Each time a function starts or ends, we write a log with the ID, whether it started or ended, and the timestamp.
#
# You are given a list logs, where logs[i] represents the ith log message formatted as a string "{function_id}:{"start" | "end"}:{timestamp}". For example, "0:start:3" means a function call with function ID 0 started at the beginning of timestamp 3, and "1:end:2" means a function call with function ID 1 ended at the end of timestamp 2. Note that a function can be called multiple times, possibly recursively.
#
# A function's exclusive time is the sum of execution times for all function calls in the program. For example, if a function is called twice, one call executing for 2 time units and another call executing for 1 time unit, the exclusive time is 2 + 1 = 3.
#
# Return the exclusive time of each function in an array, where the value at the ith index represents the exclusive time for the function with ID i.

# Constraints:
#
# 1 <= n <= 100
# 1 <= logs.length <= 500
# 0 <= function_id < n
# 0 <= timestamp <= 109
# No two start events will happen at the same timestamp.
# No two end events will happen at the same timestamp.
# Each function has an "end" log for each "start" log.
from typing import List, Tuple


class Solution:
    # or use stack, but recursive way is beautiful
    def rec(self, logs: List[str], results: List[int], id: int, ts: int, i: int) -> Tuple[int, int]:
        sub_time = 0
        i = i + 1
        while i < len(logs):
            id2, start_or_end, ts2 = logs[i].split(":")
            if id2 != id or start_or_end == "start":
                last, log_index = self.rec(logs, results, id2, ts2, i)
                i = log_index
                sub_time += last
            else:
                last = int(ts2) - int(ts) - sub_time + 1
                results[int(id)] += last
                return int(ts2) - int(ts) + 1, i + 1

    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:
        ret = [0 for i in range(n)]
        i = 0
        while i != len(logs):
            id, _, ts = logs[i].split(":")
            _, i = self.rec(logs, ret, id, ts, i)
        return ret
