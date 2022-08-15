from collections import Counter


# two pass to solve
class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        bulls, cows = 0, 0
        s, g = Counter(secret), Counter(guess)
        for i in range(len(secret)):
            if secret[i] == guess[i]:
                bulls += 1
                g[secret[i]] -= 1

        for i in range(len(secret)):
            if secret[i] != guess[i] and g[secret[i]] != 0:
                cows += 1
                g[secret[i]] -= 1

        return str(bulls) + "A" + str(cows) + "B"


# one pass
class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        bulls, cows = 0, 0
        g = Counter(guess)
        for i in range(len(secret)):
            if secret[i] == guess[i]:
                bulls += 1
                if g[secret[i]] == 0:
                    cows -= 1
                else:
                    g[secret[i]] -= 1
            else:
                if g[secret[i]] != 0:
                    cows += 1
                    g[secret[i]] -= 1

        return str(bulls) + "A" + str(cows) + "B"
