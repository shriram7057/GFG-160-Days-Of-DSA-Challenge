class Solution:
    def countAtMostK(self, arr, k):
        from collections import defaultdict

        count = 0
        left = 0
        freq = defaultdict(int)

        for right in range(len(arr)):
            freq[arr[right]] += 1

            while len(freq) > k:
                freq[arr[left]] -= 1
                if freq[arr[left]] == 0:
                    del freq[arr[left]]
                left += 1

            count += (right - left + 1)

        return count
