#思路：
今天只做了一道题，这么简单的题半小时没想出来，因为和女朋友吵了一下午，头也晕了，胃也不舒服，最近国内还闹肺炎
马上要回国了，希望一切安好，感情啊，真是折磨人的东西 2020.3.6晚 


class Solution:
    def threeSumSmaller(self, nums: List[int], target: int) -> int:
        nums.sort()
        i=0
        n=len(nums)
        count=0
        for i in range(n-2):
            j,k=i+1,n-1
            while j<k:
                if nums[i]+nums[j]+nums[k]<target:
                    count+=(k-j)
                    j+=1
                else:
                    k-=1      
        return count

        
