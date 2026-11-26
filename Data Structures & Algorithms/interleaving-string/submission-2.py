class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        # m = len(s3)
        # dp = [[0] * 2 for _ in range(m)]
        # for i, item in enumerate(s3):
        #     if s1[i] == s3[i]:
        if len(s1) + len(s2) != len(s3):
            return False
        def dp(i,j,k):
            if i == -1 and j == -1 and k == -1:
                return True
            elif i < -1 or j < -1 or k < -1:
                return False
            find = False
            print(i,j,k)
            if i >= 0 and s3[k] == s1[i]:
                find = find or dp(i-1,j,k-1)
            if j >= 0 and s3[k] == s2[j]:
                find = find or dp(i,j-1,k-1)
            return find 
        
        return dp(len(s1)-1,len(s2)-1,len(s3)-1)

