### 解题思路
一直保证一个递增的单调递增栈

### 代码

```python3
class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stack=[]
        for i in num:
            while stack and stack[-1]>i and k:
                stack.pop()
                k-=1
            stack.append(i)
        while stack and k:
            stack.pop()
            k-=1
        if not stack:
            return "0"
        tmp="".join(i for i in stack)
        return tmp.lstrip("0") or "0"
```
