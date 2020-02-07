### 解题思路
异或

### 代码

```python3
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        res=0
        for i in nums:
            res^=i
        return res
