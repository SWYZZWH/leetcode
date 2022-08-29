class Solution:
    # standard KMP implementation
    def strStr(self, haystack: str, needle: str) -> int:
        M, N = len(haystack), len(needle)

        nxt = [0 for i in range(N)]
        shadow, cur = 0, 1
        while cur < N:
            if needle[shadow] == needle[cur]:
                shadow += 1
                # notice
                nxt[cur] = shadow
                cur += 1
            elif shadow == 0:
                cur += 1
            else:
                # notice
                shadow = nxt[shadow - 1]

        i, j = 0, 0
        while i < M and j < N:
            if haystack[i] == needle[j]:
                i += 1
                j += 1
            elif j == 0:
                i += 1
            else:
                j = nxt[j - 1]

        return i - N if j == N else -1
