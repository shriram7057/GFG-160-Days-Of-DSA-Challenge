class Solution:
    def maxProduct(self,arr):
        # code here
        n=len(arr)
        result=arr[0]
        curr_max=arr[0]
        curr_min=arr[0]
        
        for i in range(1,n):
            temp = curr_max
            curr_max=max(arr[i],arr[i]*curr_max,arr[i]*curr_min)
            curr_min=min(arr[i],arr[i]*temp,arr[i]*curr_min)
            result=max(result,curr_max)
        return result 