#User function Template for python3
class Solution:
    def countWays(self, s):
        # code here
        # MOD=1003
        n=len(s)
        memo={}
        def solve(i,j,isTrue):
            if i> j:
                return 0
            if i==j:
                if isTrue:
                    return 1 if s[i]=='T' else 0
                else:
                    return 1 if s[i]=='F' else 0
            if (i, j, isTrue) in memo:
                return memo[(i,j,isTrue)]
            ways=0
            for k in range(i+1,j,2):
                op=s[k]
                lt=solve(i,k-1,True)
                lf=solve(i,k-1,False)
                rt=solve(k+1,j,True)
                rf=solve(k+1,j,False)
                
                if op=='&':
                    if isTrue:
                        ways +=lt*rt
                    else:
                        ways+=lt*rf+lf*rt+lf*rf
                elif op=='|':
                    if isTrue:
                        ways += lt*rt+lt*rf+lf*rt
                    else:
                        ways += lf *rf
                elif op =='^':
                    if isTrue:
                        ways +=lt*rf+lf*rt
                    else:
                        ways +=lt*rt+lf*rf
                # ways%=MOD
            memo[(i,j,isTrue)]=ways
            return ways
        return solve(0,n-1,True)