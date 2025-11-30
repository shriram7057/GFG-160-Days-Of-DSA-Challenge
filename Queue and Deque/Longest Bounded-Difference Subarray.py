class Solution:
    def longestSubarray(self, arr, x):
        #code here
        from collections import deque
        
        maxd=deque()
        mind=deque()
        
        l=0
        best_l=0
        best_len=1
        
        for r in range(len(arr)):
            while maxd and arr[maxd[-1]] < arr[r]:
                maxd.pop()
            maxd.append(r)
            
            while mind and arr[mind[-1]] > arr[r]:
                mind.pop()
            mind.append(r)
            
            while arr[maxd[0]] - arr[mind[0]] > x:
                if maxd[0] ==l:
                    maxd.popleft()
                if mind[0]==l:
                    mind.popleft()
                l += 1
            if r-l+1 > best_len:
                best_len = r - l + 1
                best_l= l
        return arr[best_l : best_l + best_len]
            
                