### 解题思路
考虑到可能会有重复的值,hashmap的值更新写在后面

### 代码

```python3
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
       
        hashmap={}
        for index,i  in enumerate(nums):
            if target-i in hashmap:
                return [index,hashmap[target-i]]
            hashmap[i]=index
        
            
```
