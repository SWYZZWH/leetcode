# 1604. Alert Using Same Key-Card Three or More Times in a One Hour Period

# LeetCode company workers use key-cards to unlock office doors. Each time a worker uses their key-card, the security system saves the worker's name and the time when it was used. The system emits an alert if any worker uses the key-card three or more times in a one-hour period.
#
# You are given a list of strings keyName and keyTime where [keyName[i], keyTime[i]] corresponds to a person's name and the time when their key-card was used in a single day.
#
# Access times are given in the 24-hour time format "HH:MM", such as "23:51" and "09:49".
#
# Return a list of unique worker names who received an alert for frequent keycard use. Sort the names in ascending order alphabetically.
#
# Notice that "10:00" - "11:00" is considered to be within a one-hour period, while "22:51" - "23:52" is not considered to be within a one-hour period.
import bisect
from typing import List


class Solution:
    # solve directly
    # must sort
    def timeStrToInt(self, keyTime: str) -> int:
        ts = keyTime.split(":")
        hh, mm = ts[0], ts[1]
        return int(hh) * 60 + int(mm)

    def alertNames(self, keyName: List[str], keyTime: List[str]) -> List[str]:
        timePair = [(keyName[i], self.timeStrToInt(keyTime[i])) for i in range(len(keyTime))]
        timePair.sort()
        ret = []
        for i in range(len(timePair)):
            if i < 2:
                continue
            p1, p2 = timePair[i - 2], timePair[i]
            if p1[0] != p2[0]:
                continue
            if p2[1] - p1[1] <= 60 and (len(ret) == 0 or ret[-1] != p1[0]):
                ret.append(p1[0])

        return ret
