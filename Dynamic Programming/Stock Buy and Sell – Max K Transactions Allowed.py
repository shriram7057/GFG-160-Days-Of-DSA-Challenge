class Solution:
    def maxProfit(self, prices, k):
        n = len(prices)
        if n == 0 or k == 0:
            return 0

        if k >= n // 2:
            profit = 0
            for i in range(1, n):
                if prices[i] > prices[i - 1]:
                    profit += prices[i] - prices[i - 1]
            return profit

        dp = [[0] * n for _ in range(k + 1)]

        for i in range(1, k + 1):
            max_diff = -prices[0]
            for d in range(1, n):
                dp[i][d] = max(dp[i][d - 1], prices[d] + max_diff)
                max_diff = max(max_diff, dp[i - 1][d] - prices[d])

        return dp[k][n - 1]
