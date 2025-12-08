class Solution {
  public:
    vector<int> search(string &pat, string &txt) {
        // code here
        int m=pat.size(),n=txt.size();
        vector<int>lps(m),ans;
        int len=0;
        for(int i=1;i<m;)
        {
            if(pat[i]==pat[len])lps[i++]= ++len;
            else if (len) len=lps[len-1];
            else lps[i++]=0;
        }
        int i=0,j=0;
        for(;i<n;){
            if(txt[i]==pat[j]){i++;j++;}
            if(j==m)
            {
                ans.push_back(i-j);
                j=lps[j-1];
            }else if(i<n && txt[i]!=pat[j])
            {
                if(j) j=lps[j-1];
                else i++;
            }
        }
        return ans;
    }
};