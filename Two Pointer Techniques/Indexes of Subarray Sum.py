#User function Template for python3
class Solution:
    def subarraySum(self, arr, target):
        # code here
        n=len(arr)
        curr_sum=0
        left=0
        
        for right in range(n):
            curr_sum += arr[right]
            
            while curr_sum > target and left <=right:
                curr_sum -= arr[left]
                left+=1
                
            if curr_sum==target:
                return [left + 1,right+1]
        return [-1]