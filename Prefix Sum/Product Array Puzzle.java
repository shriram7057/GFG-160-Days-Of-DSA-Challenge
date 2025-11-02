class Solution {
    public static int[] productExceptSelf(int arr[]) {
        int n = arr.length;
        int[] result = new int[n];

        // Step 1: Compute prefix products
        result[0] = 1;
        for (int i = 1; i < n; i++) {
            result[i] = result[i - 1] * arr[i - 1];
        }

        // Step 2: Multiply with suffix products
        int suffix = 1;
        for (int i = n - 1; i >= 0; i--) {
            result[i] *= suffix;
            suffix *= arr[i];
        }

        return result;
    }
}
