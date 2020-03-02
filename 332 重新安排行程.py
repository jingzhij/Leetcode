### 解题思路
因为输出有顺序，所以先排序，从大的开始加，这样保证了字母序较小的先出栈。
最后返回res[::-1]
### 代码

```python3
class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        from collections import defaultdict
        grid=defaultdict(list)
        for start,des in sorted(tickets)[::-1]:
            grid[start].append(des)
        res=[]
        def dfs(root):
            while grid[root]:
                dfs(grid[root].pop())
            res.append(root)
        dfs("JFK")
        return res[::-1]
      
```
