# 346. Moving Average from Data Stream

# Given a stream of integers and a window size, calculate the moving average of all integers in the sliding window.
#
# Implement the MovingAverage class:
#
# MovingAverage(int size) Initializes the object with the size of the window size.
# double next(int val) Returns the moving average of the last size values of the stream.

# just keep count and sum
import collections


class MovingAverage:

    def __init__(self, size: int):
        self.nums = collections.deque()
        self.count = 0
        self.sum = 0
        self.size = size

    def next(self, val: int) -> float:
        self.nums.append(val)
        self.sum += val
        if self.count != self.size - 1:
            self.count += 1
        else:
            last = self.nums.popleft()
            self.sum -= last

        return self.sum / self.count

# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)
