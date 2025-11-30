#User function Template for python3

class Solution:
    def findPermutation(self, s):
        # Code here
        res=[]
        s=sorted(s)
        used=[False]*len(s)
        
        def backtrack(path):
            if len(path)==len(s):
                res.append("".join(path))
                return
            for i in range(len(s)):
                if used[i]:
                    continue
                if i > 0 and s[i] == s[i-1] and not used[i-1]:
                    continue
                used[i]=True
                backtrack(path+[s[i]])
                used[i]=False
        backtrack([])
        return res
