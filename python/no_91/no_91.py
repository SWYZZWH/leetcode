class Solution:
    def numDecodings(self, s: str) -> int:
        decode_map = set([str(i + 1) for i in range(26)])

        @functools.cache
        def dfs(i: int) -> int:
            if i == len(s):
                return 1

            ret = 0
            if s[i] == "1":
                ret += dfs(i + 1)
                if i < len(s) - 1:
                    ret += dfs(i + 2)
            elif s[i] == "2":
                ret += dfs(i + 1)
                if i < len(s) - 1 and ord(s[i + 1]) <= ord("6"):
                    ret += dfs(i + 2)
            elif s[i] == "0":
                return 0
            else:
                ret += dfs(i + 1)

            return ret

        return dfs(0)
