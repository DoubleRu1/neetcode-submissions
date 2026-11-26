class Solution:
    def longestPalindrome(self, s: str) -> str:
        l = len(s)
        dp = [[0] * l for _ in range(l)]
        for i in range(l):
            dp[i][i] = 1
        mleft,mright = 0, 0
        ml = 1
        for i in range(1,l):
            for left in range(l-i):
                if s[left] == s[left+i] and (dp[left+1][left+i-1] != 0 or left +1 > left +i-1):
                    dp[left][left + i] = dp[left + 1][left+i-1] + 2
                    if dp[left][left+i] > ml:
                        ml = dp[left][left+i]
                        mleft, mright = left, left+i
        # for i in range(l-1):
        #     for j in range(i+1,l):
        #         if s[i] == s[j]:
        #             dp[i][j] = dp[i+1][j-1] + 2
        #             if dp[i][j] > ml:
        #                 ml = dp[i][j]
        #                 left, right = i, j
        return s[mleft:mright+1]

