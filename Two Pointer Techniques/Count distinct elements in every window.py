class Solution:
    def countDistinct(self, arr, k):
        # Code here
        n=len(arr)
        freq={}
        res=[]
        
        for i in range(k):
            freq[arr[i]]=freq.get(arr[i],0)+1
        res.append(len(freq))
        
        for i in range(k,n):
            out=arr[i-k]
            freq[out]-=1
            if freq[out]==0:
                del freq[out]
            freq[arr[i]]=freq.get(arr[i],0)+1
            res.append(len(freq))
        return res