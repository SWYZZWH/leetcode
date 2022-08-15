class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freq = [0 for i in range(26)]
        l, r = 0, 0
        ret = 0

        while r < len(s):
            while r < len(s):
                freq[ord(s[r]) - ord('A')] += 1
                r += 1
                if r - l - max(freq) > k:
                    break
                ret = max(ret, r - l)

            while r - l - max(freq) > k:
                freq[ord(s[l]) - ord('A')] -= 1
                l += 1

        return ret
