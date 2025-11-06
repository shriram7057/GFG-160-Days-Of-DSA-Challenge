class Solution:
    def minRemovals(self, arr, k):
        total = sum(arr)
        if total <= k:
            return 0

        max_len = 0
        curr_sum = 0
        left = 0

        for right in range(len(arr)):
            curr_sum += arr[right]

            while curr_sum > k:
                curr_sum -= arr[left]
                left += 1

            max_len = max(max_len, right - left + 1)

        return len(arr) - max_len
