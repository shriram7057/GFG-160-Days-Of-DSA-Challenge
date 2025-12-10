class Solution:
    def maxProfit(self, prices):
        n = len(prices)
        if n == 0:
            return 0

        # dp[i][j] = max profit using at most i transactions up to day j
        dp = [[0] * n for _ in range(3)]  # 0, 1, 2 transactions

        for i in range(1, 3):  # transaction count: 1 to 2
            max_diff = -prices[0]
            for j in range(1, n):
                dp[i][j] = max(dp[i][j - 1], prices[j] + max_diff)
                max_diff = max(max_diff, dp[i - 1][j] - prices[j])

        return dp[2][n - 1]
