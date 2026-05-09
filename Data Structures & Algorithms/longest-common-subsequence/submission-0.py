class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        if not text1 or not text2:
            return 0
        n = len(text1)
        m = len(text2)
        dp = [[0]*n for _ in range(m)]
        for j in range(n):
            if text2[0] == text1[j]:
                dp[0][j] = 1
            else:
                if j > 0:
                    dp[0][j] = dp[0][j-1]
                else:
                    dp[0][j] = 0
        for i in range(m):
            if text1[0] == text2[i]:
                dp[i][0] = 1
            else:
                if i > 0:
                    dp[i][0] = dp[i-1][0]
                else:
                    dp[i][0] = 0
        for j in range(1, n):
            for i in range(1, m):
                if text1[j] == text2[i]:
                    dp[i][j] = 1 + dp[i-1][j-1]
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])
        return dp[m-1][n-1]
             