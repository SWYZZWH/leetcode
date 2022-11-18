class Solution:
    # expr = term +- term +- term
    # term = factor */ factor */ factor
    # factor = [0-9]+ / (expr)
    def calculate(self, s: str) -> int:
        s = s.replace(" ", "")

        term_op = {
            "*": lambda x, y: x * y,
            "/": lambda x, y: int(x / y),
        }

        expr_op = {
            "+": lambda x, y: x + y,
            "-": lambda x, y: x - y,
        }

        def expr(s: str, i: int) -> (int, int):
            res, i = term(s, i)
            while i != len(s) and s[i] in expr_op:
                f = expr_op[s[i]]
                r, i = term(s, i + 1)
                res = f(res, r)
            return res, i

        def term(s: str, i: int) -> (int, int):
            res, i = factor(s, i)
            while i != len(s) and s[i] in term_op:
                f = term_op[s[i]]
                r, i = factor(s, i + 1)
                res = f(res, r)
            return res, i

        def factor(s: str, i: int) -> (int, int):
            if i == len(s):
                return 0, i
            if s[i] == "(":
                res, i = expr(s, i + 1)
                return res, i + 1
            res = 0
            while i != len(s) and s[i].isdigit():
                res *= 10
                res += int(s[i])
                i += 1
            return res, i

        return expr(s, 0)[0]