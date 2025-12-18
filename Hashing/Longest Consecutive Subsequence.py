# Longest Consecutive Subsequence

class Solution:
    def longestConsecutive(self, arr):
        num_set = set(arr)
        longest = 0

        for num in num_set:
            # Only start counting if it's the beginning of a sequence
            if num - 1 not in num_set:
                current = num
                streak = 1

                while current + 1 in num_set:
                    current += 1
                    streak += 1

                longest = max(longest, streak)

        return longest
