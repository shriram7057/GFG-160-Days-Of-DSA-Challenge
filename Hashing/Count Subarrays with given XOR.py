from collections import defaultdict

class Solution:
    def subarrayXor(self, arr, k):
        count = 0
        xor = 0
        freq = defaultdict(int)
        freq[0] = 1  # To handle subarrays starting from index 0

        for num in arr:
            xor ^= num
            count += freq[xor ^ k]
            freq[xor] += 1

        return count
