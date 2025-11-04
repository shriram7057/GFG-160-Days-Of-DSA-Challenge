class Solution:
    def countPS(self, s):
        n = len(s)
        count = 0
        dp = [[False] * n for _ in range(n)]

        for gap in range(n):
            for i in range(n - gap):
                j = i + gap
                if gap == 0:
                    dp[i][j] = True
                elif gap == 1:
                    dp[i][j] = (s[i] == s[j])
                else:
                    dp[i][j] = (s[i] == s[j]) and dp[i + 1][j - 1]
                
                if dp[i][j] and gap > 0:
                    count += 1

        return count
v