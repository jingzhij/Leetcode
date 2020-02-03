### 解题思路
首先计算正向距离，总计里减去争相距离就是反向距离，返回较小的那一个

### 代码

```python3
class Solution:
    def distanceBetweenBusStops(self, distance: List[int], start: int, destination: int) -> int:
        total=sum(distance)
        start1=min(start,destination)
        destination1=max(start,destination)
        print(start1,destination)
        part1=sum(distance[start1:destination1])
        return min(total-part1,part1)

