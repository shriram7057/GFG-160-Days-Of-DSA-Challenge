// Find All Triplets with Zero Sum

// User function Template for C++
class Solution {
  public:
    vector<vector<int>> findTriplets(vector<int> &arr) {
        // Code here
        int n = arr.size();
        vector<vector<int>> res;
        
        vector<pair<int,int>> a;
        for(int i =0 ;i<n;i++)
        {
            a.push_back({arr[i],i});
        }
        sort(a.begin(),a.end());
        for(int i = 0;i<n-2;i++)
        {
            int l = i+1;
            int r = n-1;
            
            while(l < r){
                int sum = a[i].first + a[l].first + a[r].first;
                
                if(sum == 0)
                {
                    vector<int> trip = {a[i].second,a[l].second,a[r].second};
                    sort(trip.begin(),trip.end());
                    res.push_back(trip);
                    l++;
                    r--;
                    
                    while(l < r && a[l].first == a[l-1].first)l++;
                    while(l < r && a[r].first == a[r+1].first)r--;
                    
                }
                else if (sum < 0)
                {
                    l++;
                }
                else{
                    r--;
                }
            }
        }
        sort(res.begin(),res.end());
        return res;
    }
};