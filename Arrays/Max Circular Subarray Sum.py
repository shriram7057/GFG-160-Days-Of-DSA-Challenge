class Solution:
    def maxCircularSum(self, arr):
        total_sum = sum(arr)
        
        # Standard Kadane's for max subarray sum
        max_ending_here = max_so_far = arr[0]
        for num in arr[1:]:
            max_ending_here = max(num, max_ending_here + num)
            max_so_far = max(max_so_far, max_ending_here)
        
        # Modified Kadane's for min subarray sum
        min_ending_here = min_so_far = arr[0]
        for num in arr[1:]:
            min_ending_here = min(num, min_ending_here + num)
            min_so_far = min(min_so_far, min_ending_here)
        
        # If all numbers are negative, return max_so_far
        if max_so_far < 0:
            return max_so_far
        
        # Otherwise, return max of normal and circular case
        return max(max_so_far, total_sum - min_so_far)