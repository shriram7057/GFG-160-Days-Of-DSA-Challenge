class Solution {
    // Function to find equilibrium point in the array.
    public static int findEquilibrium(int arr[]) {
        int totalSum = 0;
        for (int num : arr) {
            totalSum += num;
        }

        int leftSum = 0;
        for (int i = 0; i < arr.length; i++) {
            totalSum -= arr[i]; // now totalSum is right sum
            if (leftSum == totalSum) {
                return i; // equilibrium index
            }
            leftSum += arr[i];
        }

        return -1; // no equilibrium point
    }
}
