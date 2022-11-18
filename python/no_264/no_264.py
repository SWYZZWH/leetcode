class Solution:
    def nthUglyNumber(self, n: int) -> int:
        ugly = [1]
        two, three, five = 0, 0, 0
        while n - 1:
            cur = min(ugly[two] * 2, ugly[three] * 3, ugly[five] * 5)
            if cur != ugly[-1]:
                ugly.append(cur)
                n -= 1
            if ugly[-1] == ugly[two] * 2:
                two += 1
            elif ugly[-1] == ugly[three] * 3:
                three += 1
            else:
                five += 1

        return ugly[-1]
