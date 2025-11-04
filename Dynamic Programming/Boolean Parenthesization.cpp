// User function Template for Java
class Solution {
    static int mod = 1003;
    static HashMap<String, Integer> memo;

    static int countWays(String s) {
        memo = new HashMap<>();
        return solve(s, 0, s.length() - 1, true);
    }

    static int solve(String s, int i, int j, boolean isTrue) {
        if (i > j) return 0;
        if (i == j) {
            if (isTrue) return s.charAt(i) == 'T' ? 1 : 0;
            else return s.charAt(i) == 'F' ? 1 : 0;
        }

        String key = i + "_" + j + "_" + isTrue;
        if (memo.containsKey(key)) return memo.get(key);

        int ways = 0;
        for (int k = i + 1; k <= j - 1; k += 2) {
            char op = s.charAt(k);

            int lt = solve(s, i, k - 1, true);
            int lf = solve(s, i, k - 1, false);
            int rt = solve(s, k + 1, j, true);
            int rf = solve(s, k + 1, j, false);

            if (op == '&') {
                if (isTrue) ways += lt * rt;
                else ways += lt * rf + lf * rt + lf * rf;
            } else if (op == '|') {
                if (isTrue) ways += lt * rt + lt * rf + lf * rt;
                else ways += lf * rf;
            } else if (op == '^') {
                if (isTrue) ways += lt * rf + lf * rt;
                else ways += lt * rt + lf * rf;
            }

            ways %= mod;
        }

        memo.put(key, ways);
        return ways;
    }
}
