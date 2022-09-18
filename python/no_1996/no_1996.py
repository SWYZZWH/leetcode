from typing import List


class Solution:
    def numberOfWeakCharacters(self, properties: List[List[int]]) -> int:
        for p in properties:
            p[1] = -p[1]
        properties.sort(reverse=True)
        max_defense = 0
        ret = 0
        for p in properties:
            if max_defense > -p[1]:
                ret += 1
            max_defense = max(max_defense, -p[1])

        return ret