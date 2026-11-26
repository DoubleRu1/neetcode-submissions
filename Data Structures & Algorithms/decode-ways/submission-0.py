class Solution:
    def numDecodings(self, s: str) -> int:
        # 边界：空串或以 0 开头直接不合法
        if not s or s[0] == '0':
            return 0
        
        n = len(s)
        # dp[i] 表示前 i 个字符的解码数
        dp = [0] * (n + 1)
        dp[0] = 1      # 空串
        dp[1] = 1      # s[0] != '0' 的前提下只有一种解码
        
        for i in range(2, n + 1):
            # 1. 看最后一位（单独解码）
            if s[i - 1] != '0':
                dp[i] += dp[i - 1]
            
            # 2. 看最后两位（一起解码）
            two = s[i - 2:i]  # s[i-2]s[i-1]
            if s[i - 2] == '1' or (s[i - 2] == '2' and s[i - 1] <= '6'):
                dp[i] += dp[i - 2]
        
        return dp[n]
