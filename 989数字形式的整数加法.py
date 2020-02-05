### 解题思路
字符串转换

### 代码

```python3
class Solution:
    def addToArrayForm(self, A: List[int], K: int) -> List[int]:
        res=[]
        for i in str(int(''.join(str(i) for i in A))+K):
            res.append(i)
        return res
```
