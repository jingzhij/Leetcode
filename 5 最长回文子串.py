
思路：最长回文字串转移方程dp[i][j]=dp[i+1][j-1] if s[i]==s[j]

class Solution:
    def longestPalindrome(self, s: str) -> str:
        n=len(s)
        if n<2:
            return s
        dp=[[False] *n for _ in range(n)]
        start=0
        max_len=1
        for i in range(n):
            dp[i][i]=True
        for j in range(1,n):
            for i in range(j):
                if s[i]==s[j]:
                    if j-i<2:
                        dp[i][j]=True
                    else:   
                        dp[i][j]=dp[i+1][j-1]
                else:
                    dp[i][j]=False
                if dp[i][j]:
                    if j-i+1>max_len:
                        max_len=j-i+1
                        start=i
        return s[start:start+max_len]
                



