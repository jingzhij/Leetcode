原理：抽屉原理，如果小于零，那么说明访问过一次，加入res 


```python3
class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        res=[]
        for i in nums:
            if nums[abs(i)-1]>0:
                nums[abs(i)-1]*=-1
            else:
                res.append(abs(i))
        return res
```
