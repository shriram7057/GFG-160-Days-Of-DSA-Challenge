import heapq
class Solution:
    def kClosest(self, points, k):
        # code here
        return heapq.nsmallest(k, points,key=lambda p: p[0]**2+p[1]**2)
        
        