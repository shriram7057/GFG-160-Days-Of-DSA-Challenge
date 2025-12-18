# Subarrays with sum K

from collections import defaultdict

class Solution:
    def cntSubarrays(self, arr, k):
        count = 0
        prefix_sum = 0
        freq = defaultdict(int)
        freq[0] = 1  # To handle subarrays starting from index 0

        for num in arr:
            prefix_sum += num
            count += freq[prefix_sum - k]
            freq[prefix_sum] += 1

        return count
