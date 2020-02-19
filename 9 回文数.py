### 解题思路


### 代码

```python3
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x<0:
            return False
        return str(x)==str(x)[::-1]
```
