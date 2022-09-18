class Solution:

    # same BFS method
    def letterCombinations(self, digits: str) -> List[str]:
        m = {
            "2": ["a", "b", "c"],
            "3": ["d", "e", "f"],
            "4": ["g", "h", "i"],
            "5": ["j", "k", "l"],
            "6": ["m", "n", "o"],
            "7": ["p", "q", "r", "s"],
            "8": ["t", "u", "v"],
            "9": ["w", "x", "y", "z"]
        }

        if len(digits) == 0:
            return []

        ret = [""]
        for d in digits:
            tmp = []
            alphas = m[d]
            for i in range(len(ret)):
                for a in alphas:
                    tmp.append(ret[i] + a)
            ret = tmp

        return ret