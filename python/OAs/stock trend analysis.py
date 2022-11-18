# unsorted array, for each index, find the next k larger element
from typing import List

from sortedcontainers import SortedDict, SortedList


def nextKLarger(nums: List[int], k: int):
    sl = SortedList()
    for num in nums:
        sl.add(num)

    print(sl)
    res = []
    for i in range(len(nums)):
        idx = sl.bisect_right(nums[i])
        if 0 <= idx + k - 1 < len(sl):
            res.append(sl[idx + k - 1])
        else:
            res.append(-1)
    return res


if __name__ == "__main__":
    print(nextKLarger([1, 4, 2, 5, 3], 2))
    assert nextKLarger([1, 4, 2, 5, 3], 2) == [2, -1, 3, -1, -1]
