class Solution:
    def countSubstrings(self, s: str) -> int:
        ans = 0
        m = len(s)
        dp = [[0] * m for _ in range(m)]
        for i in range(m):
            for j in range(i,m):
                dp[i][j] = -1 
        for dis in range(m):
            for i in range(m-dis):
                if dis == 0:
                    dp[i][i+dis] =  1
                    ans += 1
                elif s[i] == s[i+dis] and dp[i+1][i+dis-1]!=-1:
                    dp[i][i+dis] = dp[i+1][i+dis-1] + 2
                    ans += 1
        return ans
