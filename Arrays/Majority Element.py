class Solution:
    def findMajority(self, arr):
        # code here
        n = len (arr)
        if not arr :
            return []
        
        count1=count2=0
        candidate1=candidate2=None 
        
        for num in arr:
            if candidate1==num:
               count1 +=1
            elif candidate2==num:
                count2 +=1
            elif count1==0:
                candidate1=num
                count1=1
            elif count2==0:
                candidate2=num
                count2=1
            else:
                count1 -=1
                count2 -=1
        result = []
        if arr.count(candidate1)>n//3:
                result.append(candidate1)
        if candidate2 != candidate1 and arr.count(candidate2)>n//3:
            result.append(candidate2)
        return sorted(result) 
               