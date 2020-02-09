### 解题思路
双指针，一前一后扫描，找到元音字母就替换
### 代码

```python3
class Solution:
    def reverseVowels(self, s: str) -> str:
        vowel="aeiouAEIOU"
        i,j=0,len(s)-1
        s=list(s)
        while i<j:
            while i<j and s[i] not in vowel:
                i+=1
            while j>i and s[j] not in vowel:
                j-=1
            if i<j:
                s[i],s[j]=s[j],s[i]
                i+=1
                j-=1
        return "".join(s)
      
```
