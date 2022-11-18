class Solution:
    def isValidSerialization(self, preorder: str) -> bool:
        vals = preorder.split(",")

        def isValid(i: int) -> (bool, int):
            if i == len(vals):
                return False, i
            if vals[i] == "#":
                return True, i + 1
            if vals[i] == "":
                return False, i
            j = 0
            while j < len(vals[i]):
                if not vals[i][j].isdigit():
                    return False, i
                j += 1
            i += 1
            l, i = isValid(i)
            if not l:
                return l, i
            r, i = isValid(i)
            if not r:
                return r, i
            return True, i

        res, i = isValid(0)
        return res and i == len(vals)