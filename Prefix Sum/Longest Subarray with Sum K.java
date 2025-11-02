// User function Template for Java
class Solution {
    public int longestSubarray(int[] arr, int k) {
        Map<Integer,Integer> prefixMap = new HashMap<>();
        int sum =0,maxLen=0;
        for(int i =0; i< arr.length;i++)
        {
            sum +=arr[i];
            if(sum==k)
                
               maxLen=i+1;
            if(prefixMap.containsKey(sum-k))
            {
                maxLen=Math.max(maxLen,i-prefixMap.get(sum-k));
            }
            if(!prefixMap.containsKey(sum))
            {
                prefixMap.put(sum,i);
            }
        }
        return maxLen;
    }
}
 {
    
}
