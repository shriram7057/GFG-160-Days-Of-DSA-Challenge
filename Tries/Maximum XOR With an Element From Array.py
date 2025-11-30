class TrieNode:
    def __init__(self):
        self.children = {}
        
class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, num):
        node = self.root
        for i in reversed(range(32)):  # 32-bit numbers
            bit = (num >> i) & 1
            if bit not in node.children:
                node.children[bit] = TrieNode()
            node = node.children[bit]
    
    def maxXor(self, num):
        node = self.root
        if not node.children:
            return -1
        max_xor = 0
        for i in reversed(range(32)):
            bit = (num >> i) & 1
            toggled = 1 - bit
            if toggled in node.children:
                max_xor |= (1 << i)
                node = node.children[toggled]
            else:
                node = node.children.get(bit, node)
        return max_xor

class Solution:
    def maxXor(self, arr, queries):
        arr.sort()
        queries = sorted([(x, m, i) for i, (x, m) in enumerate(queries)], key=lambda x: x[1])
        
        trie = Trie()
        result = [0] * len(queries)
        idx = 0
        
        for x, m, i in queries:
            while idx < len(arr) and arr[idx] <= m:
                trie.insert(arr[idx])
                idx += 1
            result[i] = trie.maxXor(x)
        
        return result
