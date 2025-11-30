class Solution:
    def power(self,b: float,e: int)-> float:
        ans=1.0
        neg=e<0
        e=abs(e)
        
        while e>0:
            if e & 1:
                ans *= b
            b *= b
            e>>=1
        return 1/ans if neg else ans