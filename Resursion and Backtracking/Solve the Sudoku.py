class Solution:
    def solveSudoku(self, mat):
        # code here
        def is_valid(r,c,val):
            b=(r//3)*3+(c//3)
            if val in row[r] or val in col[c] or val in box[b]:
                return False
            return True
        def place(r,c,val):
            mat[r][c]=val
            row[r].add(val)
            col[c].add(val)
            box[(r//3)*3+(c//3)].add(val)
        
        def remove(r,c,val):
            mat[r][c]=0
            row[r].remove(val)
            col[c].remove(val)
            box[(r//3)*3+(c//3)].remove(val)
            
        def solve():
            for r in range(9):
                for c in range(9):
                    if mat[r][c]==0:
                        for val in range(1,10):
                            if is_valid(r,c,val):
                                place(r,c,val)
                                if solve():
                                    return True
                                remove(r,c,val)
                        return False
            return True
        row=[set() for _ in range(9)]
        col=[set() for _ in range(9)]
        box=[set() for _ in range(9)]
        
        for r in range(9):
            for c in range(9):
                if mat[r][c]!=0:
                    val=mat[r][c]
                    row[r].add(val)
                    col[c].add(val)
                    box[(r//3)*3+(c//3)].add(val)
        solve()
        
                            
                            
                            
                            