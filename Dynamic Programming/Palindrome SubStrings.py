class Solution:
    def countPS(self, s):
        # code here
        t = '#' + '#'.join(s) + '#'
        n = len(t)
        
        p=[0]*n
        c = r = 0
        
        for i in range(n):
            mirror= 2*c - i
            
            if i<r:
                p[i]= min(r - i , p[mirror])
            a= i + p[i] + 1
            b=i - p[i] - 1
            
            while a < n and b >= 0 and t[a] ==t[b]:
                p[i] += 1
                a += 1
                b -=1
            if i+p[i] > r:
                c,r=i,i+p[i]
                
        count = 0
        for val in p:
            count += val // 2
        return count 