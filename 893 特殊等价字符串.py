### 解题思路
奇数位置和偶数位置排序，放到set里面

### 代码

```python3
class Solution:
    def numSpecialEquivGroups(self, A: List[str]) -> int:
        res=set()
        for s in A:
            res.add("".join(sorted(s[::2]))+"".join(sorted(s[1::2])))
     
        return len(res)



