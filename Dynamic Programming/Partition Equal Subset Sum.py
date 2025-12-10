class Solution:
    def equalPartition(self, arr):
        total = sum(arr)
        if total % 2 != 0:
            return 0  # Can't partition odd sum into two equal subsets

        target = total // 2
        n = len(arr)
        dp = [False] * (target + 1)
        dp[0] = True  # Base case: sum 0 is always possible

        for num in arr:
            for i in range(target, num - 1, -1):
                dp[i] = dp[i] or dp[i - num]

        return 1 if dp[target] else 0
