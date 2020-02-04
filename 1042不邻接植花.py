### 解题思路
感谢doudoucao大佬提供的思路
首先计算邻接矩阵，从头开始遍历，只要和周围的颜色不一样，随机选择一个就行

### 代码

```python3
class Solution:
    def gardenNoAdj(self, N: int, paths: List[List[int]]) -> List[int]:
        grid=[[] for _ in range(N)]
        for i,j in  paths:
            grid[i-1].append(j-1)
            grid[j-1].append(i-1)
        ans=[0]*N
        for i in range(N):
            ans[i]=({1,2,3,4}-{ans[i] for i in grid[i]}).pop()
        return ans


