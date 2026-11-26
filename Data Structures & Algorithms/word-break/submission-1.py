class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        m = len(s)
        dp = [False] * (m+1)
        dp[0] = True
        for i in range(1,m+1):
            for word in wordDict:
                # print(i,s[i-len(word):i],word,i-len(s))
                if i>=len(word)-1 and word == s[i-len(word):i] and dp[i-len(word)]==True:
                    dp[i] = True
                    break
        print(dp)
        return dp[-1]
                    