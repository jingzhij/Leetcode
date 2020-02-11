### 解题思路
如何是字母，则加入小写状态，如果是数字则直接加入，最后判断是否构成回文串即res==res[::-1]

### 代码

```python3
class Solution:
    def isPalindrome(self, s: str) -> bool:
        res=[]
        for char in s:
            if char.isalpha():
                res.append(char.lower())
            elif char.isdigit():
                res.append(char)
        return res==res[::-1]
```
