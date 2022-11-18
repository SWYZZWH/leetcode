class Solution:
    def reverseVowels(self, s: str) -> str:
        # two pointers
        n = len(s)
        sl = list(s)
        i, j = 0, n - 1
        while i < j:
            while i < j and sl[i].lower() not in ["a", "e", "i", "o", "u"]:
                i += 1
            while i < j and sl[j].lower() not in ["a", "e", "i", "o", "u"]:
                j -= 1
            if i == j:
                break
            sl[i], sl[j] = sl[j], sl[i]
            i += 1
            j -= 1

        return "".join(sl)
