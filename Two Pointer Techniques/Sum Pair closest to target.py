class Solution:
    def sumClosest(self, arr, target):
        # code here
        arr.sort()
        left=0
        right=len(arr)-1
        closest_sum=float('inf')
        result=[]
        while left< right:
            curr_sum=arr[left]+arr[right]
            if abs(target-curr_sum)<abs(target-closest_sum):
                closest_sum=curr_sum
                result=[arr[left],arr[right]]
            if curr_sum<target:
                left+=1
            else:
                right-=1
        return result
