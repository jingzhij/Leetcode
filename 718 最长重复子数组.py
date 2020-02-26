### 解题思路
创造一个dp数组，dp[i][j]表示以A[i]为结尾和以B[j]为结尾的最大子数组的长度
dp[i][j]=dp[i-1][j-1]+1 if A[i-1]==B[j-1] else 0
### 代码

```python3
class Solution:
    def findLength(self, A: List[int], B: List[int]) -> int:
        lenA=len(A)
        lenB=len(B)
        dp=[[0]*(lenB+1) for _ in range(lenA+1)]
        for i in range(1,lenA+1):
            for j in range(1,lenB+1):
                if A[i-1]==B[j-1]:
                    dp[i][j]=dp[i-1][j-1]+1
                else:
                    dp[i][j]=0
        return max(max(row) for row in dp)


```
