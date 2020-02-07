### 解题思路
为什么可以直接return True呢
我们可以这样想，因为是偶数排，我们把奇数索引涂成红色，偶数索引涂成黑色（涂什么颜色无所谓），由于整个的和是奇数，所以
黑色部分的和和红色部分的和，肯定有一大一小。而无论什么情况，显手的人总是能拿完全部的红色或者黑色，所以此题返回True


### 代码

```python3
class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        return True
        
```
