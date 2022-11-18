class Solution:
    def reverseWords(self, s: str) -> str:
        s = s.strip()
        if len(s) == 0:
            return s
        new_s = s[0]
        for i in range(1, len(s)):
            if s[i] == " " and s[i - 1] == " ":
                continue
            new_s += s[i]

        words = new_s.split(" ")
        return " ".join(word for word in words[::-1])