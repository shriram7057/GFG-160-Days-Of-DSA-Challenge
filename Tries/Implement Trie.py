// User function Template for Java
class TrieNode {
    TrieNode[] children;
    boolean isEnd;
    public TrieNode() {
        // Implement Trie
        children = new TrieNode[26];
        isEnd=false;
    }
}
class Trie
{
    private TrieNode root;
    public Trie()
    {
        root = new TrieNode();
    }
    // Insert a word into the Trie
    public void insert(String word) {
        TrieNode node = root ;
        for (char ch:word.toCharArray())
        {
            int idx=ch-'a';
            if (node.children[idx]==null)
            {
                node.children[idx]= new TrieNode();
            }
            node=node.children[idx];
        }
        node.isEnd=true;
    }
    

    // Search for a word in the Trie
    public boolean search(String word) {
        TrieNode node = root;
        for (char ch: word.toCharArray())
        {
            int idx = ch -'a';
            if(node.children[idx]==null)
            {
                return false;
            }
            node =node.children[idx];
        }
        return node.isEnd;
    }

    // Check if a prefix exists in the Trie
    public boolean isPrefix(String word) {
        TrieNode node = root;
        for(char ch:word.toCharArray())
        {
            int idx = ch -'a';
            if(node.children[idx]==null)
            {
                return false;
            }
            node = node.children[idx];
        }
        return true;
    }
}