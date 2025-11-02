class Solution {
  public:
    vector<int> singleNum(vector<int>& arr) {
        int xorAll = 0;
        for (int num : arr) {
            xorAll ^= num;
        }

        // Find rightmost set bit in xorAll
        int diffBit = xorAll & -xorAll;

        int x = 0, y = 0;
        for (int num : arr) {
            if (num & diffBit)
                x ^= num;
            else
                y ^= num;
        }

        // Return sorted result for consistency
        if (x < y)
            return {x, y};
        else
            return {y, x};
    }
};
