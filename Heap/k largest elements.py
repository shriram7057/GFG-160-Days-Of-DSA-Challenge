import heapq
class Solution:
    def kLargest(self, arr, k):
        # Your code here
        return heapq.nlargest(k, arr)