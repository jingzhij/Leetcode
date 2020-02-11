### 解题思路
写得有点丑，但是易于理解。dp[i]保存的是索引i的最大取值。
dp[i]=max(dp[i-1],dp[i-2]+nums[i])，这个转移方程表示要么dp[i]的值和dp[i-1]相等，即不偷第i个房子，
要么偷第i个房子，那么偷万之后的值是dp[i-2]+nums[i]

### 代码

```python3
class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        n=len(nums)
        if n==1:
            return nums[0]
        dp=[0]*n
        dp[0]=nums[0]
        dp[1]=max(nums[0],nums[1])
        for i in range(2,n):
            dp[i]=max(dp[i-1],dp[i-2]+nums[i])
        return dp[-1]




        



       
```
