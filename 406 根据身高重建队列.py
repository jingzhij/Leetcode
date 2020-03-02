### 解题思路
对身高逆序，对键值正序，先排序，
然后插入
为什么这么做？因为比它大的数字只存在与前面，按照键值进行插入一定没错

### 代码

```python3
class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        people.sort(key = lambda x:(-x[0],x[1]))
        output=[]
        for a in people:
            output.insert(a[1],a)
        return output



```
