class Solution:
    def count(self, coins, sum):
        n = len(coins)
        dp = [0] * (sum + 1)
        dp[0] = 1  # There's one way to make sum 0 — use no coins

        for coin in coins:
            for i in range(coin, sum + 1):
                dp[i] += dp[i - coin]

        return dp[sum]
