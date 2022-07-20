# 818. Race Car

# Your car starts at position 0 and speed +1 on an infinite number line. Your car can go into negative positions. Your car drives automatically according to a sequence of instructions 'A' (accelerate) and 'R' (reverse):
#
# When you get an instruction 'A', your car does the following:
# position += speed
# speed *= 2
# When you get an instruction 'R', your car does the following:
# If your speed is positive then speed = -1
# otherwise speed = 1
# Your position stays the same.
# For example, after commands "AAR", your car goes to positions 0 --> 1 --> 3 --> 3, and your speed goes to 1 --> 2 --> 4 --> -1.
#
# Given a target position target, return the length of the shortest sequence of instructions to get there.

# 1 <= target <= 104

class Solution:
    # BFS is okay and it's easy to get the instructions
    # DP is hard cause it needs to be proved, dp[i] means: the minimum instructions starting from 0 and reach i,
    # target in [2^(n - 1) - 1, 2^n - 1]
    # two strategies:
    #   go 2^n - 1 then R, then dp[2^n - 1 - target]: n + 1
    #   go 2^(n - 1), then R, then go m (m < n - 1), then R, then dp[target - (2^(n - 1) - 2^m)] : 2 + n - 1 + m
    #
    dp = {0: 0}

    def racecar(self, target: int) -> int:
        if target in self.dp:
            return self.dp[target]
        n = target.bit_length() + 1
        self.dp[target] = self.racecar(2 ** n - 1 - target) + n + 1
        for i in range(n - 1):
            self.dp[target] = min(self.dp[target], self.racecar(target - 2 ** (n - 1) - 2 ** i) + 2 + n - 1 - i)
        return self.dp[target]
