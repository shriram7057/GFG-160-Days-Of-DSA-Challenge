class Solution:
    def getMinDiff(self, arr, k):
        # code here
        n = len(arr)
        arr.sort()
        ans=arr[n-1]-arr[0]
        
        for i in range(1,n):
            if arr[i]- k <0:
                 continue
            max_height= max(arr[i-1]+k,arr[-1]-k)
            min_height= min(arr[0]+k,arr[i]-k)
            ans = min(ans,max_height - min_height)
        return ans
          