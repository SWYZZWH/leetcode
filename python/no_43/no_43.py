class Solution:
    # mock multiplication
    def multiply(self, num1: str, num2: str) -> str:
        def char2digit(s: str) -> int:
            return ord(s[0]) - ord("0")

        m, n = len(num1), len(num2)
        res = 0
        for i in reversed(range(m)):
            cur_res = ""
            flag = 0
            for j in reversed(range(n)):
                mul = char2digit(num1[i]) * char2digit(num2[j]) + flag
                flag = mul // 10
                cur_res = str(mul % 10) + cur_res
            if flag:
                cur_res = str(flag) + cur_res
            res += int(cur_res) * (10 ** (m - i - 1))

        return str(res)