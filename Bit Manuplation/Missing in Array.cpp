class Solution {
  public:
    int missingNum(vector<int>& arr) {
        int n = arr.size() + 1;
        long long total = (1LL * n * (n + 1)) / 2;
        long long sum = 0;
        for (int num : arr) {
            sum += num;
        }
        return total - sum;
    }
};
