class Solution:
    def getSecondLargest(self, arr):
        # Code Here
        if len(arr)<2:
            return -1
        first =second = float('-inf')   
        for num in arr:
            if num > first :
                second=first
                first=num 
            elif num > second and num !=first:
                second=num 
        return second if second != float('-inf') else -1