class Solution:
    def nQueen(self, n):
        # code here
        res=[]
        board=[-1]*n
        
        col=set()
        diag1 = set()
        diag2 = set()
        
        def solve(r):
            if r==n:
                res.append([board[i]+ 1 for in range(n)])
                return 
            for c in range(n):
                if c in col or (r-c) in diag1 or (r+c) in diag2:
                    continue
                board[r]=c
                col.add(c)
                diag1.add(r-c)
                diag2.add(r+c)
                
                solve(r+1)
                
                col.remove(c)
                diag1.remove(r-c)
                diag2.remove(r+c)
        solve(0)
        return res 