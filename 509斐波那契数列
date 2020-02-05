### 解题思路
自底向上构建

### 代码

```python3
class Solution:
    def fib(self, N: int) -> int:
        dp=[0]*max(2,(N+1))
        dp[1]=1
        for i in range(2,N+1):
            dp[i]=dp[i-1]+dp[i-2]
        return dp[N]


```
