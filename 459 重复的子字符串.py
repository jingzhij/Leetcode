### 解题思路
反证法 假设s不是一个字符串重复多次构成
那么 s 一定不在(s+s)[1,-1]里面，因为分别破坏了前面一个和最后一个

### 代码

```python3
class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        return s in (s+s)[1:-1]
        
        
```
