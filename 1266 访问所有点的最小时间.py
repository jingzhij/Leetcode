class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        res=0
        for i in range(1,len(points)):
            res+=max(abs(points[i][0]-points[i-1][0]), abs(points[i][1]-points[i-1][1])) #选择 x-x‘ 和 y-y'距离中最大的一个作为答案，要加绝对值
        return res
            
