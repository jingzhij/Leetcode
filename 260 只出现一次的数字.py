#思路：首先计算一个所有数字的异或值
然后计算异或值的最右侧为1的值（它必然来自于两个单独的数字之一），以它为分界线，再异或

class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        mask=0
        for num in nums:
            mask^=num
        dif=mask&(-mask)
        a=0
        for num in nums:
            if num&dif:
                a^=num
        return [a,mask^a]
