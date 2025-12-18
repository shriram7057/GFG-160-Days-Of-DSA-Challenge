# Intersection of Two arrays with Duplicate Elements
class Solution:
    def intersect(self, a, b):
        # code here
        freq={}
        for x in a:
            freq[x]=freq.get(x,0)+1
        ans=[]
        for x in b:
            if x in freq and freq[x]>0:
                ans.append(x)
                freq[x]-=1
        return sorted(list(set(ans)))