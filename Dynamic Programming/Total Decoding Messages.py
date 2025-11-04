class Solution:
    def countWays(self, digits):
        MOD = 10**9 + 7
        n = len(digits)
        if n == 0 or digits[0] == '0':
            return 0

        dp = [0] * (n + 1)
        dp[0] = 1  # Empty string has one way to decode
        dp[1] = 1  # First digit is valid (non-zero)

        for i in range(2, n + 1):
            if digits[i - 1] != '0':
                dp[i] += dp[i - 1]
            two_digit = int(digits[i - 2:i])
            if 10 <= two_digit <= 26:
                dp[i] += dp[i - 2]
            dp[i] %= MOD

        return dp[n]
