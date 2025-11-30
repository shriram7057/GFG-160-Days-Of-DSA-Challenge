
class Solution {
  public:
    char nonRepeatingChar(string &s) {
        //  code here
        unordered_map<char,int>freq;
        
        for (char ch:s)
        {
            freq[ch]++;
        }
        for (char ch:s)
        {
            if (freq[ch]== 1)
            return ch;
        }
        return '$';
    }
};