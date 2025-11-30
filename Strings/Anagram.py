class Solution {
  public:
    bool areAnagrams(string& s1, string& s2) {
        // code here
        if (s1.length()!= s2.length())
            return false;
        unordered_map<char,int>count;
        for (char ch : s1)
            count[ch]++;
        for (char ch:s2)
        {
            if (count.find(ch)==count.end())
                return false;
            count[ch]--;
            if (count[ch]<0)
                return false;
        }
        return true;
    }
};