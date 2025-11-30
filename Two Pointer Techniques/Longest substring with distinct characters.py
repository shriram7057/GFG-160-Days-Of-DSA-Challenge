class Solution:
    def longestUniqueSubstr(self, s):
        # code here
        last={}
        l=0
        ans=0
        
        for r in range(len(s)):
            ch=s[r]
            
            if ch in last and last[ch]>=l:
                l=last[ch]+1
            last[ch]=r
            ans=max(ans,r-l+1)
        return ans