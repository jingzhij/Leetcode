思路：自己定义一个key比较字符串就好了，注意结尾去0
class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        from functools import cmp_to_key
        nums=map(str,nums)
        key=cmp_to_key(lambda x,y:int(y+x)-int(x+y))
        return "".join(sorted(nums,key=key)).lstrip("0") or "0"


