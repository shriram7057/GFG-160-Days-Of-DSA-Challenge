
class Solution:
    def countTriplets(self, arr, target):
        # code here
        n=len(arr)
        count=0
        for i in range(n-2):
            l,r=i+1,n-1
            
            while l<r:
                s=arr[i]+arr[l]+arr[r]
                if s==target:
                    if arr[l]==arr[r]:
                        k=r-l+1
                        count+=(k*(k-1))//2
                        break
                    left_val=arr[l]
                    left_count=0
                    while l<r and arr[l]==left_val:
                        l+=1
                        left_count+=1
                    right_val=arr[r]
                    right_count=0
                    while r>=l and arr[r]==right_val:
                        r-=1
                        right_count+=1
                    count +=left_count * right_count
                elif s<target:
                    l += 1
                else :
                    r-=1
        return count 