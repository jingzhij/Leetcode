### 解题思路
首先只能分成四份，所以记录一下n,如果n=4并且s为空，那么是符合条件的。
其次在递归的时候判断一下是不是范围，是不是为0-255之间，如果不是，不进行递归

### 代码

```python3
class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        ans=[]
        def findIp(s,pre,n):
            if not s and n==4:
                ans.append(".".join(str(i) for i in pre))
                return 
            if n==4 and s:
                return
            if s and s[0]=="0":
                findIp(s[1:],pre+[s[:1]],n+1)
            else:
                for i in range(min(len(s),3)):
                    if s[:i+1] and  0<=int(s[:i+1])<256:
                        findIp(s[i+1:],pre+[s[:i+1]],n+1)
        findIp(s,[],0)
        return ans

```
