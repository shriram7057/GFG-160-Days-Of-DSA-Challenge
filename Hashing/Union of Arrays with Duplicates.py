# Union of Arrays with Duplicates

class Solution:    
    def findUnion(self, a, b):
        return sorted(set(a + b))
