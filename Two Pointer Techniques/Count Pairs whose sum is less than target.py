#User function Template for python3
class Solution:
    #Complete the below function
    def countPairs(self, arr, target):
        #Your code here
        arr.sort()
        count=0
        left=0
        right=len(arr)-1
        
        while left<right:
            if arr[left]+arr[right]<target:
                count+=(right-left)
                left+=1
            else:
                right-=1
        return count