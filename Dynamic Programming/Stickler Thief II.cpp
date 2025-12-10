class Solution {
  public:
    int robLinear(vector<int>& arr, int start, int end) {
        int n = end - start + 1;
        if (n == 0) return 0;
        if (n == 1) return arr[start];
        if (n == 2) return max(arr[start], arr[start + 1]);

        vector<int> dp(n);
        dp[0] = arr[start];
        dp[1] = max(arr[start], arr[start + 1]);

        for (int i = 2; i < n; ++i) {
            dp[i] = max(dp[i - 1], arr[start + i] + dp[i - 2]);
        }

        return dp[n - 1];
    }

    int maxValue(vector<int>& arr) {
        int n = arr.size();
        if (n == 0) return 0;
        if (n == 1) return arr[0];
        if (n == 2) return max(arr[0], arr[1]);

        int case1 = robLinear(arr, 0, n - 2);
        int case2 = robLinear(arr, 1, n - 1);
        return max(case1, case2);
    }
};
