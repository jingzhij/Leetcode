### 解题思路
一维dp，dp[i]=min(dp[i],dp[i-j*j]+1)

### 代码

```python3
class Solution:
    def numSquares(self, n: int) -> int:
        dp=[i for i in range(n+1)]
        for i in range(2,n+1):
            for j in range(1,int(i**(0.5))+1):
                dp[i]=min(dp[i],dp[i-j*j]+1)
        return dp[n]
```
