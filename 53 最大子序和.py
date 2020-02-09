### 解题思路
实际上是个原地dp，如果前面的总和小于零，那么就取零

### 代码

```python3
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
     
        for i in range(1,len(nums)):
            nums[i]=nums[i]+max(nums[i-1],0)
        return max(nums)



```
