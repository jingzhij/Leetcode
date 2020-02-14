### 解题思路
prefix 的key值是前n项的和，s记录到目前为止的和，如果发现s-k在prefix里面，那么就是说，prefix里面有和为k的连续项
那么它的值即为i+1-prefix[s-k]，索引是i+1因为prefix[0]占了第零位，为什么是最大值，因为当一个值出现的时候，我们记录的是它第一次出现的索引，这样的话后面如果再次出现相同的值，我们也不重写prefix，保证了i+1-prefix[s-k] 中的prefix[s-k]永远是最小的

### 代码

```python3
class Solution:
    def maxSubArrayLen(self, nums: List[int], k: int) -> int:
        n=len(nums)
        prefix={}
        prefix[0]=0
        res=0
        s=0
        for i in range(n):
            s+=nums[i]
            if s not in prefix:
                prefix[s]=i+1
            if s-k in prefix:
                res=max(res,i+1-prefix[s-k])
        return res

        





```
