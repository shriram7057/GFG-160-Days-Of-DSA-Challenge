class Solution:
    def minCoins(self, coins, sum):
        MAX = float('inf')
        dp = [MAX] * (sum + 1)
        dp[0] = 0  # Base case: 0 coins needed to make sum 0

        for i in range(1, sum + 1):
            for coin in coins:
                if coin <= i and dp[i - coin] != MAX:
                    dp[i] = min(dp[i], dp[i - coin] + 1)

        return dp[sum] if dp[sum] != MAX else -1
