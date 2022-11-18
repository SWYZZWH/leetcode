class Solution:
    # k = 2
    # dacabc
    # acabcd
    # c abcda
    # c k = 1
    # c bcdaa
    # c cdaab
    # cdaabc k = 2
    # aabccd
    def orderlyQueue(self, s: str, k: int) -> str:
        if k >= 2:
            return "".join(sorted(s))

        res = s
        for i in range(len(s)):
            new_s = s[i:] + s[:i]
            if new_s < res:
                res = new_s

        return res
