#User function Template for python3
class Solution:
    def findTriplets(self, arr):
        n = len(arr)
        result = []

        for i in range(n - 2):
            for j in range(i + 1, n - 1):
                for k in range(j + 1, n):
                    if arr[i] + arr[j] + arr[k] == 0:
                        result.append([i, j, k])

        return result
