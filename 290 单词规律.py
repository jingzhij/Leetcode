### 解题思路
建立一对一映射，如果两个都不在哈希表中，那么添加hashmap[i]=j
如果一个在一个不在，返回false，如果都在但是值不等，返回false

### 代码

```python3
class Solution:
    def wordPattern(self, pattern: str, str: str) -> bool:
        hashmap={}
        tmp=str.split()
        if len(pattern)!=len(tmp):
            return False
        for i,j in zip(pattern,str.split()):
            if i not in hashmap and j not in hashmap.values():
                hashmap[i]=j    
            elif i not in hashmap and j in hashmap.values():
                return False
            elif i in hashmap:
                if hashmap[i]!=j:
                    return False
        return True

       
```
